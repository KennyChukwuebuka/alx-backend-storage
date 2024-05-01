#!/usr/bin/env python3
"""function decorator
"""


import requests
import redis
from functools import wraps


def track_access_count(func):
    """function decorator
    """
    @wraps(func)
    def wrapper(url):
        """function decorator
        """
        # Initialize Redis client
        redis_client = redis.Redis()

        # Track the number of accesses for the URL
        access_count_key = f"count:{url}"
        redis_client.incr(access_count_key)

        return func(url)
    return wrapper


def cache_content(func):
    """function decorator
    """
    @wraps(func)
    def wrapper(url):
        # Initialize Redis client
        redis_client = redis.Redis()

        # Check if the content is cached
        cached_content = redis_client.get(url)
        if cached_content:
            return cached_content.decode()

        # Retrieve the HTML content from the URL
        html_content = func(url)

        # Cache the content with expiration time of 10 seconds
        redis_client.setex(url, 10, html_content)

        return html_content
    return wrapper


@track_access_count
@cache_content
def get_page(url: str) -> str:
    """function decorator
    """
    response = requests.get(url)
    return response.text
