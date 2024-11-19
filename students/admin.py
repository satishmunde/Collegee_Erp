# student/admin.py
from django.contrib import admin
from .models import Student, Attendance

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'enrollment_number', 'department')
    search_fields = ('name', 'enrollment_number')
    list_filter = ('department',)

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'date', 'status')
    list_filter = ('date', 'status', 'course')
