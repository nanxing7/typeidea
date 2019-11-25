#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019/11/20 04:00
# @Author  : 三哥
# @Site    : 
# @File    : serializers.py
# @Software: PyCharm

from rest_framework import serializers, pagination

from .models import Post, Category


class PostSerializer(serializers.HyperlinkedModelSerializer):
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

    url = serializers.HyperlinkedIdentityField(view_name='api-post-detail')

    class Meta:
        model = Post
        fields = ['url', 'id', 'title', 'category', 'tags', 'owner', 'created_time']


class PostDetailSerializer(PostSerializer):
    class Meta:
        model = Post
        fields = ['url', 'id', 'title', 'category', 'tags', 'owner', 'content_html', 'created_time']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'created_time',)


class CategoryDetailSerializer(CategorySerializer):
    posts = serializers.SerializerMethodField('paginated_posts')

    def paginated_posts(self, obj):
        """实现对某个分类下文章列表的获取和分页"""
        posts = obj.post_set.filter(status=Post.STATUS_NORMAL)
        paginator = pagination.PageNumberPagination()
        page = paginator.paginate_queryset(posts, self.context['request'])
        serializer = PostSerializer(page, many=True, context={'request': self.context['request']})
        return {
            'count': posts.count(),
            'results': serializer.data,
            'previous': paginator.get_previous_link(),
            'next': paginator.get_next_link(),
        }

    class Meta:
        model = Category
        fields = (
            'id', 'name', 'created_time', 'posts'
        )
