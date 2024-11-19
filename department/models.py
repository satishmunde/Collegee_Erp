# department/models.py
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)
    head = models.ForeignKey('administration.Admin', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
