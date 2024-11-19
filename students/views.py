from rest_framework import viewsets
from rest_framework.response import Response
from .models import Student, Attendance
from .serializers import StudentSerializer, AttendanceSerializer
from django.shortcuts import get_object_or_404

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.select_related('department').all()
    serializer_class = StudentSerializer

    # Enable partial update by setting `partial=True`
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.select_related('student', 'course').all()
    serializer_class = AttendanceSerializer
