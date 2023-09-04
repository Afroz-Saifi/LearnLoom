from django.db import models

# Create your models here.
from CourseApp.models import Course  # Import the Course model from the CourseApp
from django.utils import timezone

class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
