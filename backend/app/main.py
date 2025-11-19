from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from .database import engine, get_db, Base
from . import models
from .twilio_webhook import router as twilio_router
from .schemas import ReviewOut

# IMPORTANT: Create tables ONLY AFTER DB ready
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(twilio_router)

@app.get("/")
def health():
    return {"status": "Backend Running"}

@app.get("/api/reviews", response_model=list[ReviewOut])
def get_reviews(db: Session = Depends(get_db)):
    return db.query(models.Review).all()
