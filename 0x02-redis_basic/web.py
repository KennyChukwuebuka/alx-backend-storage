#!/usr/bin/env python3
"""function decorator
"""


import requests
import redis


def get_page(url: str) -> str:
    """
    A function that retrieves the HTML content of a given URL.
    Parameters:
        url (str): The URL to fetch the content from.
    Returns:
        str: The HTML content of the URL.
    """
    # Initialize Redis client
    redis_client = redis.Redis()

    # Track the number of accesses for the URL
    access_count_key = f"count:{url}"
    redis_client.incr(access_count_key)

    # Check if the content is cached
    cached_content = redis_client.get(url)
    if cached_content:
        return cached_content.decode()

    # Retrieve the HTML content from the URL
    response = requests.get(url)
    html_content = response.text

    # Cache the content with expiration time of 10 seconds
    redis_client.setex(url, 10, html_content)

    return html_content
