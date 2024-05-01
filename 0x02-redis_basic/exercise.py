#!/usr/bin/env python3
"""Cache class
"""


import uuid
import redis
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator function that counts the number of calls made to a method.

    Args:
        method (Callable): The method to be wrapped.

    Returns:
        Callable: The wrapped method that increments the call count in Redis.

    Raises:
        None

    Example:
        @count_calls
        def my_method(self, arg1, arg2):
            # Method implementation
            pass
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        A function that acts as a wrapper for the input method,
        incrementing the call count in Redis.

        Args:
            self: The instance of the class.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            The result of calling the input method with the
            provided arguments and keyword arguments.
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    def __init__(self):
        """
        Initializes a new instance of the Cache class.

        This method creates a new instance of the
        Cache class and initializes the
        `_redis` attribute with a new instance of
        the Redis client. It also flushes
        the entire Redis database by calling the
        `flushdb` method on the Redis client.

        Parameters:
            None

        Returns:
            None
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """func
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] =
            None) -> Union[str, bytes, int, float, None]:
        """func
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> Union[str, None]:
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        return self.get(key, fn=int)
