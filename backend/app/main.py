from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from .database import engine, get_db, Base
from . import models
from .twilio_webhook import router as twilio_router
from .schemas import ReviewOut

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Twilio webhook router
app.include_router(twilio_router)

@app.get("/")
def health():
    return {"status": "Backend Running"}

# -------------------------
# GET ALL REVIEWS
# -------------------------
@app.get("/api/reviews", response_model=list[ReviewOut])
def get_reviews(db: Session = Depends(get_db)):
    return db.query(models.Review).all()

# -------------------------
# DELETE REVIEW (FIXED)
# -------------------------
@app.delete("/api/review/{review_id}")
def delete_review(review_id: int, db: Session = Depends(get_db)):
    review = db.query(models.Review).filter(models.Review.id == review_id).first()

    if not review:
        return {"message": "Review not found"}

    db.delete(review)
    db.commit()
    return {"message": "Review deleted successfully"}
