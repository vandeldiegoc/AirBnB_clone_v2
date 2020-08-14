#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade='all, delete', backref='state')

    else:    
        @property
        def cities(self):
            """return obj list"""
            new_list = []
            obj = models.storage.all(City)
            for key, value in obj.items():
                if value.state_id == self.id:
                    new_list.append(value)
            return new_list

        name = ""
