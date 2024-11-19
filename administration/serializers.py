# administration/serializers.py
from rest_framework import serializers
from .models import Admin

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'
        extra_kwargs = {'name': {'required': False}, 'email': {'required': False}}

    def validate_email(self, value):
        if not value.endswith('@college.edu'):
            raise serializers.ValidationError("Email must be from college.edu domain.")
        return value

    def validate_role(self, value):
        allowed_roles = ['Super Admin', 'Admin']
        if value not in allowed_roles:
            raise serializers.ValidationError("Role must be either 'Super Admin' or 'Admin'.")
        return value
