# models/post.py
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    caption = Column(Text)
    hash_tags = Column(Text)
    media_type = Column(String(20))
    media_description = Column(Text)