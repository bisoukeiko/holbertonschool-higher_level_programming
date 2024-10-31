#!/usr/bin/python3
""" Python - Object-relational mapping
    task100:
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    Difinetion of the states table
        id: an auto-generated, unique integer, can’t be null, is a primary key
        name: Name of the state string, maximum 128 characters, cannot be null)
        cities (City): The related City object
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="State", cascade="all, delete")