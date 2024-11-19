# student/models.py
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True)
    enrollment_number = models.CharField(max_length=50, unique=True)
    date_of_birth = models.DateField()
    department = models.ForeignKey('department.Department', on_delete=models.CASCADE)
    admission_date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.enrollment_number})"


class Attendance(models.Model):
    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
    ]

    student = models.ForeignKey('students.Student', on_delete=models.CASCADE)
    course = models.ForeignKey('course.Course', on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    class Meta:
        unique_together = ('student', 'course', 'date')

    def __str__(self):
        return f"{self.student} - {self.course} on {self.date}: {self.status}"
