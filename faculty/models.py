# faculty/models.py
from django.db import models

class Faculty(models.Model):
    ROLE_CHOICES = [
        ('Professor', 'Professor'),
        ('Assistant Professor', 'Assistant Professor'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True)
    department = models.ForeignKey('department.Department', on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.role})"
