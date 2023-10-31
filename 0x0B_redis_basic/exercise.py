#!/usr/bin/env python3
"""
exercise.py
"""
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ count_calls method"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrapper method"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """ Cache class"""

    def __init__(self):
        """ constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store method"""
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str, fn: Optional[Callable] = None) -> \
            Union[str, bytes, int, float]:
        """ get method"""
        data = self._redis.get(key)
        if data is None:
            return None
        return data if fn is None else fn(data)

    def get_str(self, key: str) -> Optional[str]:
        """ get_str method"""
        data = self.get(key, fn=lambda d: d.decode("utf-8"))
        return data

    def get_int(self, key: str) -> Optional[int]:
        """ get_int method"""
        data = self.get(key, fn=lambda d: int(d.decode("utf-8")))
        return data
