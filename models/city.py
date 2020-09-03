#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
import os


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship('Place', backref='cities', cascade='all, delete')

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """return the list of City objects"""
            city_l = []
            all_city = model.storage.all(City)
            for city in all_city.value():
                if city.state_id == self.id:
                    all_city.append(city)
            return all_city
