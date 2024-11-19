# faculty/admin.py
from django.contrib import admin
from .models import Faculty

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'role', 'department')
    search_fields = ('name', 'email')
    list_filter = ('role', 'department')
