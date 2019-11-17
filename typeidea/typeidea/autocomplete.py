#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/17 4:35
# @Author  : 三哥
# @Site    :
# @File    : autocomplete.py
# @Software: PyCharm


from dal import autocomplete

from blog.models import Category, Tag


class CategoryAutocomplete(autocomplete.Select2QuerySetView):
    @property
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Category.objects.none()

        qs = Category.objects.filter(owner=self.request.user).order_by(
            'id')  # 加入order_by 解决警告UnorderedObjectListWarning问题

        if self.q:  # q 是从 url 传递来的值
            qs = qs.filter(name__istartswith=self.q)
        return qs


class TagAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Tag.objects.none()

        qs = Tag.objects.filter(owner=self.request.user).order_by('id')

        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs
