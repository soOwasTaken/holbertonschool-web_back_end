#!/usr/bin/env python3
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    """
    User model for the users table
    """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)


engine = create_engine('sqlite:///example.db', echo=False)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_user = User(
    email='example@example.com',
    hashed_password='hashedpassword',
    session_id='sessionid',
    reset_token='resettoken'
)

session.add(new_user)
session.commit()
