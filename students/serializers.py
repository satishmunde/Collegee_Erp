# student/serializers.py
from rest_framework import serializers
from .models import Student, Attendance

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        extra_kwargs = {'name': {'required': False}, 'email': {'required': False}}

    def validate_enrollment_number(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Enrollment number must be numeric.")
        return value

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'
        extra_kwargs = {'date': {'required': False}}

    def validate_status(self, value):
        if value not in ['Present', 'Absent']:
            raise serializers.ValidationError("Status must be either 'Present' or 'Absent'.")
        return value
