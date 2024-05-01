#!/usr/bin/env python3
"""Cache class
"""


import uuid
import redis
from typing import Callable
from functools import wraps


def call_history(method: Callable) -> Callable:
    """function call_history
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """function wrapper
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
        """function __init__
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    def store(self, data):
        """function store
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
