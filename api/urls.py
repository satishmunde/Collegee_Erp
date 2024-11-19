# project_name/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from administration.views import AdminViewSet
from department.views import DepartmentViewSet
from faculty.views import FacultyViewSet
from students.views import StudentViewSet, AttendanceViewSet
from course.views import CourseViewSet, EnrollmentViewSet
from examination.views import ExamViewSet, GradeViewSet

router = DefaultRouter()
router.register(r'admins', AdminViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'faculty', FacultyViewSet)
router.register(r'students', StudentViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'exams', ExamViewSet)
router.register(r'grades', GradeViewSet)

urlpatterns = [

    path('', include(router.urls)),
]
