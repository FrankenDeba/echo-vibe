# routers/post.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.post import PostCreate, PostIdea, PostSkeleton
from typing import List
from utils.database import get_db
from utils.auth import get_current_user
from services.post_service import create_multiple_post, generate_idea, generate_posts, create_post
from utils.profile import has_business_profile
from schemas.business_profile import BusinessProfileCreate

router = APIRouter()

@router.post("/generate-idea")
def idea(
    t3_info: PostIdea, 
    business_info: bool | BusinessProfileCreate = Depends(has_business_profile())
    ):
    return generate_idea(t3_info=t3_info, business_info=business_info)

@router.post("/generate-post")
def create_posts(
    post_skeleton:PostSkeleton, 
    business_info: bool | BusinessProfileCreate = Depends(has_business_profile())
    ):
    return generate_posts( post_skeleton.selected_ideas,post_skeleton.t3_info, business_info)

@router.get("/")
def list_posts():
    return {"msg": "List all posts"}

@router.post("/")
def create(
    post_data: PostCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return create_post(db = db, user_id=current_user["id"], post_data=post_data)

@router.post("/multiple")
def create_many_posts(
    post_data: List[PostCreate],
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return create_multiple_post(db = db, user_id=current_user["id"], post_data=post_data)

@router.put("/{id}")
def update_post(id: int):
    return {"msg": f"Post {id} updated"}

@router.delete("/{id}")
def delete_post(id: int):
    return {"msg": f"Post {id} deleted"}