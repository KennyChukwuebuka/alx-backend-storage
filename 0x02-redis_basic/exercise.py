#!/usr/bin/env python3
"""Redis basic
"""


import uuid
import redis
from typing import Callable
from functools import wraps


def call_history(method: Callable) -> Callable:
    """
    A decorator function to store input and output
    history of a method using Redis.

    Parameters:
    method (Callable): The method to be wrapped.

    Returns:
    Callable: The wrapped method that stores
    input and output history.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        A decorator function that wraps another function.
        Stores input arguments in Redis before
        executing the original method.
        Stores the output of the original method in Redis as well.
        Returns the output of the original method.
        """
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"

        # Store input arguments
        self._redis.rpush(inputs_key, str(args))

        # Execute the original method
        output = method(self, *args, **kwargs)

        # Store output
        self._redis.rpush(outputs_key, output)

        return output
    return wrapper


class Cache:
    def __init__(self):
        """
        Initializes a new instance of the class.

        This method creates a new instance of the
        class and initializes the `_redis` attribute
        with a new Redis client. It then flushes the
        entire Redis database by calling the
        `flushdb()` method on the `_redis` client.

        Parameters:
            None

        Returns:
            None
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    def store(self, data):
        """
        A description of the entire function,
        its parameters, and its return types.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
