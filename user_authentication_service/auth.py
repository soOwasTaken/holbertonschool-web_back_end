#!/usr/bin/env python3
"""DB AUTH"""

import bcrypt
from db import DB
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import User


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    @staticmethod
    def _hash_password(password: str) -> bytes:
        """
        Hash a password using bcrypt, return the hashed password as bytes.
        """
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password

    def register_user(self, email: str, password: str) -> User:
        """Register a user and return the User object."""
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = self._hash_password(password)
            return self._db.add_user(email, hashed_password)
        else:
            raise ValueError(f'User {email} already exists')
