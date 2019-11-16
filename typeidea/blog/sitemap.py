#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019/11/16 13:45
# @Author  : 三哥
# @Site    : 
# @File    : sitemap.py
# @Software: PyCharm

from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Post


class PostSitemap(Sitemap):
    changefreq = "always"
    priority = 1.0
    protocol = 'https'

    def items(self):
        """返回所有正常状态的文章"""
        return Post.objects.filter(status=Post.STATUS_NORMAL)

    def lastmod(self, obj):
        """返回每篇文章的创建时间/更新时间"""
        return obj.created_time

    def location(self, obj):
        """返回每篇文章的 URL"""
        return reverse('post-detail', args=[obj.pk])
