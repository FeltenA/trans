from django.contrib import admin
from .models import User

@admin.register(User)
class AllUsersAdmin(admin.ModelAdmin):
    list_display = ("nickname", "name", "password")