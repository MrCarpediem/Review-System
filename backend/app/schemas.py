from pydantic import BaseModel
from datetime import datetime

class ReviewCreate(BaseModel):
    phone: str
    user_name: str
    product_name: str
    rating: int
    product_review: str

class ReviewOut(BaseModel):
    id: int
    phone: str
    user_name: str
    product_name: str
    rating: int
    product_review: str
    created_at: datetime   # VERY IMPORTANT

    class Config:
        from_attributes = True
