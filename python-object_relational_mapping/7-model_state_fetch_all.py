#!/usr/bin/python3
""" Python - Object-relational mapping
    task07
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main():
    """
    Display all State objects from the database hbtn_0e_6_usa

    Args:
        sys.argv[1] (str): Username for MySQL authentication.
        sys.argv[2] (str): Password for MySQL authentication.
        sys.argv[3] (str): Database name to connect to.
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    SessionClass = sessionmaker(engine)
    session = SessionClass()

    results = session.query(State).order_by(State.id).all()

    for state in results:
        print("{}: {}".format(state.id, state.name))
    session.close()


if __name__ == "__main__":
    main()
