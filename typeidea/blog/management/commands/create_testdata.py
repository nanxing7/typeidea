#!/usr/bin/env python  这一行Linux上才需要
# -*- coding: utf-8 -*-
# @Time    : 2019/11/19 18:45
# @Author  : 三哥
# @Site    : 
# @File    : create_testdata.py
# @Software: PyCharm

from django.core.management.base import BaseCommand
from blog.models import Post, Tag, Category
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'create test datas'

    def handle(self, *args, **options):
        user = get_user_model().objects.get_or_create(email='test@test.com', username='测试用户',
                                                      password='test!q@w#eTYU')[0]
        self.stdout.write(self.style.SUCCESS('created test datas \n'))
