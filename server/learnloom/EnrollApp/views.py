from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Enroll
from CourseApp.models import Course  # Import the Course model from the CourseApp

@csrf_exempt  # Only for development; remove in production and use proper authentication.
def add_enrollment(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from request body
            data = json.loads(request.body.decode('utf-8'))

            # Create a new Enroll instance
            enrollment = Enroll(
                user_id=data.get('user'),      # Assuming 'user' is the user ID
                course_id=data.get('course'),  # Assuming 'course' is the course ID
            )

            # Save the enrollment to the database
            enrollment.save()

            # Return a success response
            return JsonResponse({'message': 'Enrollment added successfully'})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt  # Only for development; remove in production and use proper authentication.
def get_user_enrollments(request, user_id):
    if request.method == 'GET':
        try:
            # Retrieve user enrollments with course details
            enrollments = Enroll.objects.filter(user_id=user_id).select_related('course')
            enrollments_with_details = []

            for enrollment in enrollments:
                enrollment_data = {
                    'user': enrollment.user_id,
                    'course': enrollment.course_id,
                    'date': enrollment.date,
                    'courseDetails': {
                        'id': enrollment.course.id,
                        'image': enrollment.course.image,
                        'instructor': enrollment.course.instructor.username,
                        'title': enrollment.course.title,
                        'description': enrollment.course.description,
                    }
                }
                enrollments_with_details.append(enrollment_data)

            return JsonResponse(enrollments_with_details, safe=False)

        except Enroll.DoesNotExist:
            return JsonResponse([], safe=False)

    return JsonResponse({'error': 'Invalid request method'}, status=405)