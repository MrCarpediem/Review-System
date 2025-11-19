from fastapi import APIRouter, Form
from .database import SessionLocal
from .models import Review
from datetime import datetime

router = APIRouter()

user_sessions = {}

@router.post("/twilio-webhook")
def twilio_webhook(From: str = Form(...), Body: str = Form(...)):
    phone = From.replace("+", "")
    msg = Body.strip()

    if phone not in user_sessions or msg.lower() in ["hi", "hello", "start"]:
        user_sessions[phone] = {"step": "name"}
        return {"message": "What's your name?"}

    session = user_sessions[phone]

    # STEP 1 — NAME
    if session["step"] == "name":
        session["name"] = msg
        session["step"] = "product"
        return {"message": "Which product is this review for?"}

    # STEP 2 — PRODUCT
    if session["step"] == "product":
        session["product"] = msg
        session["step"] = "rating"
        return {"message": "Give rating (1-5)."}

    # STEP 3 — RATING
    if session["step"] == "rating":
        # Validate rating is number
        if not msg.isdigit():
            return {"message": "Rating must be a number between 1-5."}

        rating = int(msg)
        if rating < 1 or rating > 5:
            return {"message": "Rating must be a number between 1-5."}

        session["rating"] = rating
        session["step"] = "review"
        return {"message": "Write your review."}

    # STEP 4 — REVIEW TEXT
    if session["step"] == "review":
        review_text = msg

        db = SessionLocal()
        review = Review(
            phone=phone,
            user_name=session["name"],
            product_name=session["product"],
            rating=session["rating"],
            product_review=review_text,
            created_at=datetime.utcnow()
        )
        db.add(review)
        db.commit()
        db.refresh(review)
        db.close()

        del user_sessions[phone]

        return {
            "message": f"Thanks {review.user_name}! Your review for {review.product_name} has been saved."
        }
