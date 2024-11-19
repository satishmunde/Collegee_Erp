# course/admin.py
from django.contrib import admin
from .models import Course, Enrollment

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_code', 'name', 'credits', 'department', 'faculty')
    search_fields = ('name', 'course_code')
    list_filter = ('department',)

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrollment_date')
    list_filter = ('course', 'enrollment_date')
