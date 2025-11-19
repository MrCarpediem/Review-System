from sqlalchemy import Column, Integer, String, Text, DateTime, func
from .database import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    phone = Column(String, nullable=False)
    user_name = Column(String, nullable=False)
    product_name = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)
    review_text = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class ConversationState(Base):
    __tablename__ = "conversation_state"

    id = Column(Integer, primary_key=True, index=True)
    phone = Column(String, index=True)
    step = Column(String)

    temp_name = Column(String, nullable=True)
    temp_product = Column(String, nullable=True)
    temp_rating = Column(Integer, nullable=True)
