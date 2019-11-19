#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019/11/19 14:45
# @Author  : 三哥
# @Site    : 
# @File    : custom_site.py
# @Software: PyCharm

from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = 'Typeidea'
    site_title = 'Typeidea 管理后台'
    index_title = '首页'

    def __init__(self, name='admin'):
        super().__init__(name)

    def has_permission(self, request):
        return request.user.is_superuser


custom_site = CustomSite(name='cus_admin')
