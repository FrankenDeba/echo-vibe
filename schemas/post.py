from pydantic import BaseModel
from typing import List, Optional

class MediaDescription(BaseModel):
    image: Optional[str] = None
    video_storyboard: Optional[str] = None
    voiceover_or_song: Optional[str] = None
    tips: List[str]

    class Config:
        extra = "allow"



class Media(BaseModel):
    type: str
    description: Optional[MediaDescription]


class PostCreate(BaseModel):
    caption: str
    hash_tags: List[str]
    media: Media

class PostUpdate(PostCreate):
    caption: Optional[str]

class PostIdea(BaseModel):
    tone: str
    target: str
    topic: str

class SelectedPostIdea(BaseModel):
    idea_title: str
    angle: str
    relevance_to_trends: str
    keyword_focus: List[str]


class PostSkeleton(BaseModel):
    selected_ideas: List[SelectedPostIdea]
    t3_info: PostIdea
