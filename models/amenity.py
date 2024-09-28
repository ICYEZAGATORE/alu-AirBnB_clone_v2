#!/usr/bin/python3
""" Amenity Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    """Represents an Amenity for a place"""
    
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)

    # Relationship with Place through the place_amenity table
    place_amenities = relationship("Place", secondary="place_amenity", viewonly=False)
