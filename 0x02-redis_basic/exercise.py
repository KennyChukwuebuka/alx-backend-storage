#!/usr/bin/env python3
"""Cache class
"""


import uuid
import redis
from typing import Union


class Cache:
    def __init__(self):
        """
        Initialize a new instance of the Cache class.

        This method initializes the Redis connection
        and flushes the entire database.

        Parameters:
            None

        Returns:
            None
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the given data in Redis and return a
        unique key for the stored data.

        Parameters:
            data (Union[str, bytes, int, float]):
            The data to be stored in Redis.

        Returns:
            str: A unique key generated using
            UUID for the stored data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
