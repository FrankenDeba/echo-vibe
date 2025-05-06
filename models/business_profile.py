from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from database import Base

class BusinessProfile(Base):
    __tablename__ = "business_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    category = Column(String(100), nullable=True)
    industry = Column(String(100), nullable=True)
    tagline = Column(String(255), nullable=True)
    website = Column(String(255), nullable=True)
    location = Column(String(100), nullable=True)
    uniqueness = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=datetime.now())

    user = relationship("User", back_populates="business_profile")
