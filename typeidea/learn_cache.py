#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019/11/25 12:28
# @Author  : 三哥
# @Site    : 
# @File    : learn_cache.py
# @Software: PyCharm
import functools
import time
from my_lrucache import LRUCacheDict


def cache_it(maxsize=1024, expiration=60):
    CACHE = LRUCacheDict(max_size=maxsize, expiration=expiration)

    def wrapper(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            key = repr(*args, **kwargs)
            try:
                result = CACHE['key']
            except KeyError:
                result = func(*args, **kwargs)
                CACHE[key] = result
            return result

        return inner

    return wrapper


@cache_it(maxsize=10, expiration=3)
def query(sql):
    result = f'execute {sql}'
    return result


if __name__ == '__main__':
    start = time.time()
    query('SELECT * FROM blog_post')
    print(time.time() - start)

    start = time.time()
    query('SELECT * FROM blog_post')
    print(time.time() - start)
