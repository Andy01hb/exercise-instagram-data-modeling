import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    posts = relationship("Post", backref="user")
    comments = relationship("Comment", backref="user")
    likes = relationship("Like", backref="user")

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    image_url = Column(String(250), nullable=False)
    description = Column(String(500))
    user_id = Column(Integer, ForeignKey('user.id'))
    comments = relationship("Comment", backref="post")
    likes = relationship("Like", backref="post")

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    text = Column(String(500), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    user = relationship("User", backref="user_comments")
    post = relationship("Post", backref="post_comments")

class Like(Base):
    __tablename__ = 'like'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    user = relationship("User", backref="user_likes")
    post = relationship("Post", backref="post_likes")

def to_dict(self):
    return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e
