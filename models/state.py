#!/usr/bin/python2
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    state = relationship("City", cascade="all, delete-orphan", backref="state")

    @property
    def cities(self):
        from models import storage
        from models.city import City
        obj_list = []
        city_obj_dict = storage.all(City)
        for city_obj in city_obj_dict.values():
            if  city_obj.state_id == self.id:
                obj_list.append(city_obj)
        return obj_list
	
    
