# department/serializers.py
from rest_framework import serializers
from .models import Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
        extra_kwargs = {'name': {'required': False}}

    def validate_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Department name should only contain alphabetic characters.")
        return value
