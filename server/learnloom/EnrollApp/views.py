from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Enroll

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
