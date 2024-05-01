#!/usr/bin/env python3
"""Cache class
"""


import uuid
import redis
from typing import Callable
from functools import wraps


def call_history(method: Callable) -> Callable:
    """function that returns the history of
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """function that returns the history of
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
        """function that returns the history of
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    def store(self, data):
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def replay(self, method: Callable):
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"

        inputs = self._redis.lrange(inputs_key, 0, -1)
        outputs = self._redis.lrange(outputs_key, 0, -1)

        print(f"{method.__qualname__} was called {len(inputs)} times:")
        for input_args, output in zip(inputs, outputs):
            input_args = eval(input_args.decode())
            print(f"{method.__qualname__}(*{input_args}) -> {output.decode()}")
