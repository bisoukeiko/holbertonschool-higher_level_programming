#!/usr/bin/python3
""" Python - Object-relational mapping
    task06:
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Difinetion of the states table
        id: an auto-generated, unique integer, can’t be null, is a primary key
        name: Name of the state string, maximum 128 characters, cannot be null)
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
