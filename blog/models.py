from core.db import Base
from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from user.models import User


class Post(Base):
    __tablename__ = "blog_posts"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String(length=100), )
    text = Column(Text, )
    user = Column(Integer, ForeignKey("user.id"))
    user_id = relationship(User)
    date = Column(DateTime)

