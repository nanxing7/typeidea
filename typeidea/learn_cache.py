#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019/11/25 12:28
# @Author  : 三哥
# @Site    : 
# @File    : learn_cache.py
# @Software: PyCharm
import functools
import time

CACHE = {}


def cache_it(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        key = repr(*args, **kwargs)
        result = CACHE.get(key)
        if not result:
            result = func(*args, **kwargs)
            CACHE[key] = result
        return result

    return inner


@cache_it
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
