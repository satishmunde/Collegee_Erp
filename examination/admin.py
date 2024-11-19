# examination/admin.py
from django.contrib import admin
from .models import Exam, Grade

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('course', 'exam_type', 'date')
    list_filter = ('exam_type', 'date')

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'exam', 'grade')
    list_filter = ('grade', 'course')
