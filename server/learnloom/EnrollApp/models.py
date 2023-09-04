from django.db import models

# Create your models here.
from user.models import User  # Import the User model from the UserApp
from CourseApp.models import Course  # Import the Course model from the CourseApp
from django.utils import timezone

class Enroll(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Enrollment for {self.user.username} in {self.course.title} on {self.date}"
