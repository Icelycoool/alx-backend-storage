#!/usr/bin/env python3
""" Web file"""
import redis
import requests
from functools import wraps
from typing import Callable

client = redis.Redis()


def track_get_page(fn: Callable) -> Callable:
    """Decorator for get_page"""
    @wraps(fn)
    def wrapper(url: str) -> str:
        """Wrapper"""
        client.incr(f'count:{url}')
        cached_page = client.get(f'{url}')
        if cached_page:
            return cached_page.decode('utf-8')
        response = fn(url)
        client.set(f'{url}', response, 10)
        return response
    return wrapper


@track_get_page
def get_page(url: str) -> str:
    """ Makes a http request to a given endpoint"""
    response = requests.get(url)
    return response.text
