from pydantic import BaseModel

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

    class Config:
        from_attributes = True
