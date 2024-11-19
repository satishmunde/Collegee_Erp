# course/models.py
from django.db import models
from students.models import *

class Course(models.Model):
    course_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    credits = models.IntegerField()
    department = models.ForeignKey('department.Department', on_delete=models.CASCADE)
    faculty = models.ForeignKey('faculty.Faculty', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.course_code})"


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey('course.Course', on_delete=models.CASCADE)
    enrollment_date = models.DateField()

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student} enrolled in {self.course}"
