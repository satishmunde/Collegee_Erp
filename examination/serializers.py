# examination/serializers.py
from rest_framework import serializers
from .models import Exam, Grade

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'

    def validate_exam_type(self, value):
        allowed_types = ['Midterm', 'Final', 'Quiz',"UT"]
        if value not in allowed_types:
            raise serializers.ValidationError("Exam type must be 'Midterm', 'Final', 'UI' or 'Quiz'.")
        return value

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'

    def validate_grade(self, value):
        allowed_grades = ['A', 'B', 'C', 'D', 'F']
        if value not in allowed_grades:
            raise serializers.ValidationError("Grade must be one of 'A', 'B', 'C', 'D', or 'F'.")
        return value
