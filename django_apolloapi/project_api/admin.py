from apolloapi.api.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

import logging

logger = logging.getLogger(__name__)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ("password", "date_joined", "last_login")
    list_display = ("username", "email", "first_name", "last_name", "is_staff")
