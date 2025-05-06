from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.business_profile import BusinessProfileCreate,BusinessProfileUpdate, BusinessProfileOut
from services.business_profile_service import create_business_profile, get_business_profile_by_user , update_business_profile, delete_business_profile
from utils.database import get_db
from utils.auth import get_current_user
from utils.profile import has_business_profile

router = APIRouter()

@router.post("/business-details")
def create_business_details(
    profile_data: BusinessProfileCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
    existing: bool | BusinessProfileCreate = Depends(has_business_profile(expect_profile=False))
):
    return create_business_profile(db, user_id=current_user["id"], profile_data=profile_data)

@router.get("/business-details")
def get_business_details(
    existing: bool | BusinessProfileCreate = Depends(has_business_profile())
):
    return existing

@router.put("/business-details", response_model=BusinessProfileOut)
def edit_business_details(
    profile_data: BusinessProfileUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
    existing: bool | BusinessProfileCreate = Depends(has_business_profile())
):
    return update_business_profile(db, user_id=current_user["id"], profile_data = profile_data, profile = existing)

@router.delete("/business-details", status_code=status.HTTP_204_NO_CONTENT)
def remove_business_details(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
    existing: bool | BusinessProfileCreate = Depends(has_business_profile())
):
    delete_business_profile(db, user_id=current_user["id"],profile=existing)
    return {"detail": "Business profile deleted successfully"}

