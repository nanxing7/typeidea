#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019/11/17 11:08
# @Author  : 三哥
# @Site    : 
# @File    : apis.py
# @Software: PyCharm

from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import Post, Category
from .serializers import PostSerializer, PostDetailSerializer, CategorySerializer, CategoryDetailSerializer


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    """提供文章接口"""
    queryset = Post.objects.filter(status=Post.STATUS_NORMAL)
    # TODO:学习 serializer_class
    serializer_class = PostSerializer

    # TODO:学习 retrieve
    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = PostDetailSerializer
        return super().retrieve(request, *args, **kwargs)

    # TODO:学习 filter_queryset
    def filter_queryset(self, queryset):
        """重写 filter_queryset 实现过滤"""
        category_id = self.request.query_params.get('category')  # 获取 url 上 Query 的 category 参数
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(status=Category.STATUS_NORMAL)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = CategoryDetailSerializer
        return super().retrieve(request, *args, **kwargs)
