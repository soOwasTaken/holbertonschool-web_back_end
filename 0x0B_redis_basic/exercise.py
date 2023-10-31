#!/usr/bin/env python3
"""
exerrcise.py
"""
import redis
import uuid
from typing import Union, Optional


class Cache:
    """ Cache class"""

    def __init__(self):
        """ constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store method"""
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key
