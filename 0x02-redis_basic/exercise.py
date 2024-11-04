#!/usr/bin/env python3
"""Cache file"""
import redis
import uuid
from typing import Union, Optional, Callable, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """"
    Decorator for the Cache method taht tracks the number of calls
    """
    @wraps(method)
    def wrapper(self: Any, *args, **kwargs) -> str:
        """
        Wraps called method and adds its call count redis before execution
        """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator for the Cache method that  tracks args
    """
    @wraps(method)
    def wrapper(self: Any, *args) -> str:
        """
        Wraps called method and tracks its passed arguments.
        """
        self._redis.rpush(f'{method.__qualname__}:inputs', str(args))
        output = method(self, *args)
        self._redis.rpush(f'{method.__qualname__}:outputs', output)
        return output
    return wrapper


class Cache:
    """
    A simple cavhe class that uses redis
    """
    def __init__(self) -> None:
        """
        Initializes the Cache class instance and flushes he Redis database
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data in the cache and returns a unique key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """Retrieves data from the Cache using the given key"""
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, data: bytes) -> str:
        """Coverts data to strings"""
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """Converts data to integers"""
        return int(data)
