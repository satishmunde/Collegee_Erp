# administration/admin.py
from django.contrib import admin
from .models import Admin

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'role')
    search_fields = ('name', 'email', 'role')
    list_filter = ('role', 'department')
