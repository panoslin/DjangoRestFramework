#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by panos on 2022/5/26
# IDE: PyCharm

from django.contrib.auth.backends import ModelBackend
from ..models import User


class ADBackend(ModelBackend):
    """
    https://www.sipios.com/blog-tech/automatic-login-in-a-django-application-using-external-authentication
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        print(username, password)
        # 1. auth in AD group
        is_auth = self.ad_auth(username, password)
        # 2. return django User object if authenticated
        if is_auth:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                user = User(username=username)
                user.is_active = True
                user.is_staff = False
                user.save()
            return user

    def ad_auth(self, username, password):
        print(username, password)
        return True
