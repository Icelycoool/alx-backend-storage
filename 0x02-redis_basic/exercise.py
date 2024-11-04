#!/usr/bin/env python3
"""Cache file"""
import redis
import uuid
from typing import Union


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

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data in the cache and returns a unique key.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored.

        Returns:
            str: The unique key assigned to the stored data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
