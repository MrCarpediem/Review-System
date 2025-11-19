from sqlalchemy.orm import Session
from . import models, schemas

def get_state(db: Session, phone: str):
    return db.query(models.ConversationState).filter_by(phone=phone).first()

def save_state(db: Session, state):
    db.add(state)
    db.commit()
    db.refresh(state)

def delete_state(db: Session, state):
    db.delete(state)
    db.commit()

def create_review(db: Session, payload: schemas.ReviewCreate):
    obj = models.Review(
        phone=payload.phone,
        user_name=payload.user_name,
        product_name=payload.product_name,
        rating=payload.rating,
        review_text=payload.review_text,
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj
