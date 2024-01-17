#!/usr/bin/python3
"""Defines State class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
import models
import os


class State(BaseModel, Base):
    """State class implementation"""
    __tablename__ = 'states'

    if os.getenv('HBNB_TYPE_STORAGE') == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", passive_deletes=True)
    else:
        name = ""

    @property
    def cities(self):
        """Returns all cities in a State"""
        return [city for city in State.cities if city.state_id == self.id]
