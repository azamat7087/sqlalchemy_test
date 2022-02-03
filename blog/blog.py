from fastapi import APIRouter, Depends, Body
from .schemas import PostCreate, PostList
from sqlalchemy.orm import Session
from core.utils import get_db
from typing import List
from . import service

router = APIRouter()


@router.get("/", response_model=List[PostList])
def post_list(db: Session = Depends(get_db)):

    posts = service.get_post_list(db)

    return posts


@router.post("/")
def post_list(item: PostCreate = Body(..., ),
              db: Session = Depends(get_db)):

    post = service.create_post(db, item)

    return post



