# administration/models.py
from django.db import models

class Admin(models.Model):
    ROLE_CHOICES = [
        ('Registrar', 'Registrar'),
        ('Department Head', 'Department Head'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    # department = models.ForeignKey('department.Department', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.role})"
