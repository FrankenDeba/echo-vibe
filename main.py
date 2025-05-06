# main.py
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, profile, post
from database import engine
import models.user, models.post

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.user.Base.metadata.create_all(bind=engine)
models.post.Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth")
app.include_router(profile.router, prefix="/profile")
app.include_router(post.router, prefix="/posts")

