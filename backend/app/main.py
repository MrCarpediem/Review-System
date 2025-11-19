from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from .database import engine, get_db
from . import models, crud, schemas
from .twilio_webhook import router as twilio_router


# Create all tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Review Collector API",
    description="WhatsApp-based Review Collection System",
    version="1.0.0",
)

# Allow frontend / Postman / Browser
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Twilio Webhook Route
app.include_router(twilio_router)


# Health Check
@app.get("/")
def root():
    return {"message": "Review Collector Backend is Running!"}


# Fetch All Saved Reviews
@app.get("/api/reviews", response_model=list[schemas.ReviewOut])
def get_reviews(db: Session = Depends(get_db)):
    return db.query(models.Review).all()


# Create Review Manually (Optional)
@app.post("/api/reviews", response_model=schemas.ReviewOut)
def create_review(payload: schemas.ReviewCreate, db: Session = Depends(get_db)):
    return crud.create_review(db, payload)
