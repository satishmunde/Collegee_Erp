# examination/models.py
from django.db import models

class Exam(models.Model):
    EXAM_TYPE_CHOICES = [
        ('Midterm', 'Midterm'),
        ('Final', 'Final'),
        ('UT', 'UT'),
        ('Quiz', 'Quize'),
    ]

    course = models.ForeignKey('course.Course', on_delete=models.CASCADE)
    exam_type = models.CharField(max_length=50, choices=EXAM_TYPE_CHOICES)
    date = models.DateField()

    def __str__(self):
        return f"{self.course} - {self.exam_type} on {self.date}"


class Grade(models.Model):
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE)
    course = models.ForeignKey('course.Course', on_delete=models.CASCADE)
    exam = models.ForeignKey('examination.Exam', on_delete=models.CASCADE)
    grade = models.CharField(max_length=5)

    class Meta:
        unique_together = ('student', 'course', 'exam')

    def __str__(self):
        return f"{self.student} - {self.course} ({self.exam.exam_type}): {self.grade}"
