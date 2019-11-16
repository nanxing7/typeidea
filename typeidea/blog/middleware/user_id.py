#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019/11/16 11:56
# @Author  : 三哥
# @Site    : 
# @File    : user_id.py
# @Software: PyCharm


import uuid

USER_KEY = 'uid'
TEN_YEARS = 60 * 60 * 24 * 365 * 10


class UserIdMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        uid = self.generate(request)
        request.uid = uid  # 将 uid 赋值给 request 对象，因为 request 是一个类的实例，可以动态赋值，可以让 View 拿到 uid 使用
        response = self.get_response(request)
        response.set_cookie(USER_KEY, uid, max_age=TEN_YEARS, httponly=True)

    def generate(self, request):
        try:
            uid = request.COOKIES(USER_KEY)  # 判断 COOKIES 中是否有 'uid' 的 COOKIES
        except KeyError:
            uid = uuid.uuid4().hex  # 生成唯一的 uid
        return uid
