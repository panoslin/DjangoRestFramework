#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by panos on 2022/5/26
# IDE: PyCharm
from .models import Article
import rest_framework_filters as filters


class ArticleFilter(filters.FilterSet):
    status = filters.MultipleChoiceFilter(field_name='status', choices=Article.status_choices)

    class Meta:
        model = Article
        fields = {
            "title": ['icontains'],
            "desc": ['icontains'],
            "content": ['icontains'],

            "author__username": ['exact'],

            "created_at": ["lte", "gte"],
            "updated_at": ["lte", "gte"],
        }
