from django.db import models

# Create your models here.
from django.db import models
from InstructorApp.models import Instructor  # Import the Instructor model from the InstructorApp

class Course(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=255)

    def __str__(self):
        return self.title
