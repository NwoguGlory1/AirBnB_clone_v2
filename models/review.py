#!/usr/bin/python3
"""Defines Review class"""
from os import getenv, environ
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import Table, Float, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """Implementation for the Review class"""
    __tablename__ = 'reviews'
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
