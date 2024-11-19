# course/serializers.py
from rest_framework import serializers
from .models import Course, Enrollment

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        extra_kwargs = {'name': {'required': False}}

    def validate_credits(self, value):
        if not (1 <= value <= 6):
            raise serializers.ValidationError("Credits must be between 1 and 6.")
        return value

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'
