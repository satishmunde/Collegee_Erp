from rest_framework import viewsets
from .models import Course, Enrollment
from .serializers import CourseSerializer, EnrollmentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.select_related('department', 'faculty').all()
    serializer_class = CourseSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.select_related('student', 'course').all()
    serializer_class = EnrollmentSerializer
