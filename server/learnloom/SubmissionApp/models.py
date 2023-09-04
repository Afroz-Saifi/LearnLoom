from django.db import models

# Create your models here.
from user.models import User  # Import the User model from the UserApp
from AssignmentApp.models import Assignment  # Import the Assignment model from the AssignmentApp

class Submission(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    submissionLink = models.CharField(max_length=255)
    username = models.CharField(max_length=255)

    def __str__(self):
        return f"Submission by {self.username} for {self.assignment.title}"
