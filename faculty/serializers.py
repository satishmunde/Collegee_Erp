from rest_framework import serializers
from .models import Faculty

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'
        extra_kwargs = {'name': {'required': False}, 'email': {'required': False}}

    def validate_email(self, value):
        if '@' not in value:
            raise serializers.ValidationError("Invalid email address.")
        return value
