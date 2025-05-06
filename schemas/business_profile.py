from pydantic import BaseModel
from typing import List, Optional

class BusinessProfileCreate(BaseModel):
    name: str
    description: Optional[str] = None
    category: Optional[str] = None
    industry: Optional[str] = None
    tagline: Optional[str] = None
    website: Optional[str] = None
    location: Optional[str] = None
    uniqueness: Optional[str] = None


class BusinessProfileUpdate(BusinessProfileCreate):
    name: Optional[str] = None

class BusinessProfileOut(BusinessProfileUpdate):
    id: int
    user_id: int

    class Config:
        from_attributes = True