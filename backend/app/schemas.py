from pydantic import BaseModel

class ReviewCreate(BaseModel):
    phone: str
    user_name: str
    product_name: str
    rating: int
    review_text: str

class ReviewOut(BaseModel):
    id: int
    phone: str
    user_name: str
    product_name: str
    rating: int
    review_text: str

    class Config:
        orm_mode = True
