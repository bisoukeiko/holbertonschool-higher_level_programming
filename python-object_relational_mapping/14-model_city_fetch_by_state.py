#!/usr/bin/python3
""" Python - Object-relational mapping
    task14
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """
    Display all City objects from the database hbtn_0e_14_usa

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

    results = session.query(
        State.name, City.id, City.name). \
        filter(State.id == City.state_id).order_by(City.id).all()

    for row in results:
        print("{}: ({}) {}".format(row[0], row[1], row[2]))
    session.close()


if __name__ == "__main__":
    main()
