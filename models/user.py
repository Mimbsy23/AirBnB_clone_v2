#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"  # Fixed typo in __tablename__
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))  # Added closing parenthesis

