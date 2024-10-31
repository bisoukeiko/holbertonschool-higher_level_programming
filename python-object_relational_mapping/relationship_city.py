#!/usr/bin/python3
""" Python - Object-relational mapping
    task100:
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.schema import ForeignKey
from relationship_state import Base, State
from sqlalchemy.orm import relationship


class City(Base):
    """
    Difinetion of the cities table
        id: an auto-generated, unique integer, can’t be null, is a primary key
        name: Name of the state, string, maximum 128 characters, can't be null
        state_id: State id,integer,can’t be null,is a foreign key to states.id
        state (State): The related State object
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    state = relationship("State", back_populates="cities")