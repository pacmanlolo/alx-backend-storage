#!/usr/bin/env python3
"""get_page function using the requests module to fetch the
content of a URL and cache it using a decorator.
"""
import redis
import requests
r = redis.Redis()
count = 0


def get_page(url: str) -> str:
    """Define the key for caching."""
    r.set(f"cached:{url}", count)
    resp = requests.get(url)
    r.incr(f"count:{url}")
    r.setex(f"cached:{url}", 10, r.get(f"cached:{url}"))
    return resp.text


if __name__ == "__main__":
    get_page("http://slowwly.robertomurray.co.uk")
