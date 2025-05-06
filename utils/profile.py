from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from models.business_profile import BusinessProfile
from .database import get_db  # Adjust the import path based on your project
from .auth import get_current_user

def has_business_profile(expect_profile = True):
    def _has_business_profile(db: Session = Depends(get_db),user =  Depends(get_current_user)):
        existing = db.query(BusinessProfile).filter(BusinessProfile.user_id == user["id"]).first()

        if expect_profile and not existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No business profile exists for this user."
            )
        
        if existing and not expect_profile:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Business profile already exists for this user."
            )
        
        return existing
    return _has_business_profile
