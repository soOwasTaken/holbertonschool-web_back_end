#!/usr/bin/env python3
"""DB AUTH"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt, return the hashed password as bytes.
    """
    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password
