#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by panos on 2022/5/26
# IDE: PyCharm
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('article', views.ArticleViewSet, 'article')

urlpatterns = [
    path('', include(router.urls))
]
