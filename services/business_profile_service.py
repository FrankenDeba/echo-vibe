from sqlalchemy.orm import Session
from models.business_profile import BusinessProfile
from schemas.business_profile import BusinessProfileCreate, BusinessProfileUpdate

def create_business_profile(db: Session, user_id: int, profile_data: BusinessProfileCreate):
    profile = BusinessProfile(**profile_data.model_dump(), user_id=user_id)
    db.add(profile)
    db.commit()
    db.refresh(profile)
    return profile

def get_business_profile_by_user(db: Session, user_id: int):
    business_profile = db.query(BusinessProfile).filter(BusinessProfile.user_id == user_id).first()
    return business_profile

def update_business_profile(db: Session, user_id: int, profile_data: BusinessProfileUpdate, profile: BusinessProfileCreate):
    for field, value in profile_data.dict(exclude_unset=True).items():
        setattr(profile, field, value) 
    db.commit()
    db.refresh(profile)
    return profile

def delete_business_profile(db: Session, user_id: int, profile: BusinessProfileCreate):
    db.delete(profile)
    db.commit()