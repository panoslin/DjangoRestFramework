#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by panos on 2022/5/26
# IDE: PyCharm
from rest_framework import (
    serializers,
    exceptions,
    permissions,
    pagination
)
from .models import Article
from login.models import User


class PaginationSerializer(pagination.PageNumberPagination):
    page_size = 12
    page_query_param = 'size'


class ArticleListSerializer(serializers.ModelSerializer):
    # permission_classes = [
    #     permissions.IsAuthenticatedOrReadOnly
    # ]

    updated_at = serializers.DateTimeField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    authorname = serializers.CharField(source='author.username', read_only=True)
    status = serializers.ChoiceField(write_only=True, choices=Article.status_choices)

    class Meta:
        model = Article
        fields = [
            'id',

            'status',
            'status_display',

            'updated_at',
            'created_at',

            'author',
            'authorname',

            'title',
            'desc',
            'content',
        ]
