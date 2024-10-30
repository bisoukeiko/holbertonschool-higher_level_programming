#!/usr/bin/python3
""" Python - Object-relational mapping
    task10
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """
    Display the states.id of the State object with the name passed
    as argument from the database hbtn_0e_6_usa.
    If no state has the name you searched for, display Not found.

    Args:
        sys.argv[1] (str): Username for MySQL authentication.
        sys.argv[2] (str): Password for MySQL authentication.
        sys.argv[3] (str): Database name to connect to.
        sys.argv[4] (str): State name to search.
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    SessionClass = sessionmaker(bind=engine)
    session = SessionClass()

    parameter = sys.argv[4]
    result = session.query(State.id).filter(State.name == parameter).first()

    if result:
        print("{}".format(result.id))
    else:
        print("Not found")

    session.close()


if __name__ == "__main__":
    main()
