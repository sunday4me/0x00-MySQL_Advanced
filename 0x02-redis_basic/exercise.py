#!/usr/bin/env python3
"""
Module - exercise
"""
import json
import redis
import uuid
from typing import Union, Callable, Any
import functools


def count_calls(method: Callable) -> Callable:
    """
    decorator takes a single method argument
    and returns a new function that wraps
    the original method
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """
        gets the qualified name of the method using the __qualname__ attribute
        and uses it as the Redis key to store the count of calls.
        It then increments the count using the Redis INCR
        """

        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    decorated function’s qualified name and append ":inputs" and ":outputs"
    to create input and output list keys, respectively.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """
        wrapped function to retrieve the output.
        Store the output using rpush in the "...:outputs" list,
        then return the output.
        """

        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"

        self._redis.rpush(input_key, str(args))

        output = method(self, *args, **kwargs)

        self._redis.rpush(output_key, output)

        return output
    return wrapper


class Cache:
    """cache in a redis storage"""
    def __init__(self, host='localhost', port=6379) -> None:
        """initialize"""
        self._redis = redis.Redis(host=host, port=port)
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store the data by setting key and data"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key, fn=None):
        """get method that take a key string argument"""
        data = self._redis.get(key)

        if fn:
            return fn(data)

        return data

    def get_str(self, key):
        """parametrize wit the correct conversion fun"""
        return self.get(key, fn=str)

    def get_int(self, key):
        """parametrize wit the correct conversion fun"""
        return self.get(key, fn=int
