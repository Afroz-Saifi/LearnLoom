from django.db import models

# Create your models here.

class Instructor(models.Model):
    ROLE_CHOICES = [
        ("student", "Student"),
        ("instructor", "Instructor"),
    ]

    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="instructor")

    def __str__(self):
        return self.username
