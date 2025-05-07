# routers/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserOut, UserLogin
from models.user import User
from utils.auth import get_password_hash, verify_password, create_access_token
from utils.database import get_db
from services.auth_service import signup as register, login

router = APIRouter()



@router.post("/signup")
def signup(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    new_user = register(db=db, user=user)
    if(new_user):
        return new_user
         
    return  HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Could not register ",
    )

@router.post("/login")
def signin(user: UserLogin, db: Session = Depends(get_db)):
    return login(db=db, user=user)

@router.post("/logout")
def logout():
    return {"message": "Logged out (client should discard token)"}