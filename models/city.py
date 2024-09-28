#!/usr/bin/python3
"""This module defines a class City"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """This class defines a city by various attributes"""
    
    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    # Relationship to Place with cascading delete
    places = relationship("Place", backref="city", cascade="all, delete")
