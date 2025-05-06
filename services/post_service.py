from sqlalchemy.orm import Session
from models.post import Post
from schemas.post import PostCreate, PostUpdate, PostIdea
from schemas.business_profile import BusinessProfileCreate 
from fastapi import HTTPException, status
from typing import List
from promts.generate_ideas_promt import generate_idea_prompt
from promts.generate_posts_promt import generate_posts_prompt
from datetime import datetime, timedelta
from llm import call_llm_pai

def create_post(db: Session, user_id: int, post_data: PostCreate):
    post = Post(
        user_id=user_id,
        caption=post_data.caption,
        hash_tags=",".join(post_data.hash_tags),
        media_type=post_data.media.type,
        media_description=post_data.media.description.json()  # store as string
    )
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def create_multiple_post(db: Session, user_id: int, post_data: List[PostCreate]):
    inserted = []
    for post_details in post_data:
        post = create_post(db=db, user_id=user_id, post_data=post_details)
        inserted.append(post)
    return inserted

def get_posts(db: Session, user_id: int):
    return db.query(Post).filter(Post.user_id == user_id).all()

def get_post_by_id(db: Session, user_id: int, post_id: int):
    post = db.query(Post).filter(Post.id == post_id, Post.user_id == user_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return post

def update_post(db: Session, user_id: int, post_id: int, post_data: PostUpdate):
    post = get_post_by_id(db, user_id, post_id)
    for key, value in post_data.model_dump(exclude_unset=True).items():
        setattr(post, key, value)
    db.commit()
    db.refresh(post)
    return post

def delete_post(db: Session, user_id: int, post_id: int):
    post = get_post_by_id(db, user_id, post_id)
    db.delete(post)
    db.commit()

def generate_idea(t3_info: PostIdea, business_info: BusinessProfileCreate):
    # Call the function
    messages = generate_idea_prompt(t3_info, business_info)
    return call_llm_pai(messages)

def generate_posts(selected_ideas,t3_info: PostIdea, business_info: BusinessProfileCreate):
    # Call the function
    messages = generate_posts_prompt(selected_ideas,t3_info, business_info)
    return call_llm_pai(messages)
