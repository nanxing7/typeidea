#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019/11/20 04:00
# @Author  : 三哥
# @Site    : 
# @File    : serializers.py
# @Software: PyCharm

from rest_framework import serializers

from .models import Post, Category


class PostSerializer(serializers.ModelSerializer):
    """文章序列化器"""
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name',
    )
    tags = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name',
    )
    owner = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )
    created_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M-%S")

    class Meta:
        model = Post
        fields = ['id', 'title', 'category', 'tags', 'owner', 'created_time']


class PostDetailSerializer(PostSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'category', 'tags', 'owner', 'content_html', 'created_time']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'created_time',)
