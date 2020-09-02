#!/usr/bin/python3
"""Place Module for HBNB project."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
import models
from os import getenv


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             nullable=False))


class Place(BaseModel, Base):
    """A place to stay."""

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship('Review', backref='place', cascade='all, delete')
    amenities = relationship(
            'Amenity', secondary=place_amenity,
            viewonly=False)

    if getenv("HBNB_TYPE_STORAGE") != 'db':
        def reviews(self):
                """ getter method"""
                r_list = []
                for obj in models.storage.all(Review).values():
                    if obj.place_id == self.id:
                        r_list.append(obj)
                return r_list

        @amenities.setter
        def amenities(self, value):
            """setter method"""
            if type(value) != Amenity:
                return
            amenity_ids = []
            self.amenity_ids.append(value)

        @property
        def amenities(self):
            """ getter method"""
            amenities_list = []
            from models import storage
            dictionary = storage.all(Amenity)
            if dictionary:
                for k, v in dictionary.items():
                    if self.id == v.place_id:
                        a_list.append(v)
            return a_list
