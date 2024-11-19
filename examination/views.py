# examination/views.py
from rest_framework import viewsets
from .models import Exam, Grade
from .serializers import ExamSerializer, GradeSerializer

class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.select_related('course')
    serializer_class = ExamSerializer

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.select_related('student', 'course', 'exam')
    serializer_class = GradeSerializer
