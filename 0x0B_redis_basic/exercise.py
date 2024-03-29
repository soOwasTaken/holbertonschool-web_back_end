#!/usr/bin/env python3
"""
exercise.py
"""
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def call_history(method: Callable) -> Callable:
    """ call_history method"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrapper method"""
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(input_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))
        return result

    return wrapper


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

    @call_history
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


def replay(method: Callable):
    """Display the history of calls of a particular function."""
    calls_count = method.__self__._redis.get(
        method.__qualname__).decode("utf-8")
    inputs_key = f"{method.__qualname__}:inputs"
    outputs_key = f"{method.__qualname__}:outputs"
    inputs_list = method.__self__._redis.lrange(inputs_key, 0, -1)
    outputs_list = method.__self__._redis.lrange(outputs_key, 0, -1)

    print(f"{method.__qualname__} was called {calls_count} times:")
    for i, (input_args, output) in enumerate(zip(inputs_list, outputs_list)):
        print(f"{method.__qualname__}(*{input_args.decode('utf-8')}) -> "
              f"{output.decode('utf-8')}")
