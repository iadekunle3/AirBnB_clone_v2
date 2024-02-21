#!/usr/bin/python3
<<<<<<< HEAD
"""This is the user class"""
from sqlalchemy.ext.declarative import declarative_base
=======
"""This module defines a class User"""
>>>>>>> fcaef794d3b575daa4ad54f672346d84388ab896
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review


class User(BaseModel, Base):
<<<<<<< HEAD
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="user")
    reviews = relationship("Review", cascade='all, delete, delete-orphan',
                           backref="user")
=======
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    places = relationship('Place', cascade='all, delete, delete-orphan',
                          backref='user')

    reviews = relationship('Review', cascade='all, delete, delete-orphan',
                           backref='user')
>>>>>>> fcaef794d3b575daa4ad54f672346d84388ab896
