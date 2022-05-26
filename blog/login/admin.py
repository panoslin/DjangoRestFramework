from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as ParentUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(ParentUserAdmin):
    list_display = ('username', 'staff_id')
    fieldsets = list(ParentUserAdmin.fieldsets) + [(None, {'fields': ('staff_id',)})]
