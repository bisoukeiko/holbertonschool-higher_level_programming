#!/usr/bin/python3
""" Python - Object-relational mapping
    task100
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """
    Create the State “California” with the City “San Francisco”
    from the database hbtn_0e_100_usa.

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

    new_state = State(name='California')
    session.add(new_state)
    session.commit()

    new_city = City(name='San Francisco', state_id=new_state.id)
    session.add(new_city)

    session.commit()
    session.close()


if __name__ == "__main__":
    main()
