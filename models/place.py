#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.amenity import Amenity
import models

# Define the place_amenity table for the Many-to-Many relationship
place_amenity = Table(
    'place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
)

class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    amenities = relationship('Amenity', secondary=place_amenity, viewonly=False)
    
    # Ensure the Amenity class has a corresponding relationship attribute
    class Amenity(BaseModel, Base):
        """ Amenity class """
        
        __tablename__ = 'amenities'
        
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place', secondary=place_amenity, viewonly=False)

    # For FileStorage
    @property
    def amenities(self):
        """Getter for amenities in FileStorage"""
        if models.storage_t != 'db':
            return [amenity for amenity in models.storage.all(Amenity).values() if amenity.id in self.amenity_ids]

    @amenities.setter
    def amenities(self, obj):
        """Setter for amenities in FileStorage"""
        if isinstance(obj, Amenity) and obj.id not in self.amenity_ids:
            self.amenity_ids.append(obj.id)
