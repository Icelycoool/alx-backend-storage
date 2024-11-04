#!/usr/bin/env python3
"""Web file"""
import redis
import requests
from functools import wraps
from typing import Callable


def track_get_page(fn: Callable) -> Callable:
    """Decorator for get_page"""
    @wraps(fn)
    def wrapper(url: str) -> str:
        """Wrapper"""
        client = redis.Redis()
        client.incr(f'count:{url}')
        cached_page = client.get(f'{url}')
        if cached_page:
            return cached_page.decode('utf-8')
        respose = fn(url)
        client.set(f'{url}', response, 10)
        return response
    return wrapper


@track_get_page
def get_page(url: str) -> str:
    """"Makes request to a particular url and gets the HTML content"""
    resposne = requests.get(url)
    return response.text
