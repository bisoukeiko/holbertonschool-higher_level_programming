#!/usr/bin/python3
""" Python - Object-relational mapping
    task11
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """
    Add the State object “Louisiana” to the database hbtn_0e_6_usa.
    Display the new states.id after creation.

    Args:
        sys.argv[1] (str): Username for MySQL authentication.
        sys.argv[2] (str): Password for MySQL authentication.
        sys.argv[3] (str): Database name to connect to.
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    SessionClass = sessionmaker(bind=engine)
    session = SessionClass()

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    result = session.query(State.id).filter(State.name == 'Louisiana').one()

    print("{}".format(result.id))

    session.close()


if __name__ == "__main__":
    main()
