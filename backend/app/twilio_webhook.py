from fastapi import APIRouter, Form, Depends, Request
from sqlalchemy.orm import Session
from .database import get_db
from . import crud, models, schemas, utils, conversation_state

router = APIRouter()

@router.post("/twilio-webhook")
async def webhook(
    request: Request,
    From: str = Form(...),
    Body: str = Form(...),
    db: Session = Depends(get_db)
):
    phone = utils.normalize_phone(From)
    text = Body.strip()

    state = crud.get_state(db, phone)
    if not state:
        state = models.ConversationState(phone=phone, step="start")
        crud.save_state(db, state)

    step = state.step
    next_step, msg = conversation_state.next_prompt(step, text)

    if step == "ask_name" and next_step == "ask_product":
        state.temp_name = text

    if step == "ask_product" and next_step == "ask_rating":
        state.temp_product = text

    if step == "ask_rating" and next_step == "ask_review":
        state.temp_rating = int(text)

    if next_step == "save":
        review = schemas.ReviewCreate(
            phone=phone,
            user_name=state.temp_name,
            product_name=state.temp_product,
            rating=state.temp_rating,
            review_text=text,
        )
        crud.create_review(db, review)
        crud.delete_state(db, state)
        return {"message": "Review saved successfully!"}

    if next_step == "cancel":
        crud.delete_state(db, state)
        return {"message": "Cancelled."}

    state.step = next_step
    crud.save_state(db, state)

    return {"message": msg}
