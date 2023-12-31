from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Course

@csrf_exempt  # Only for development; remove in production and use proper authentication.
def add_course(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from request body
            data = json.loads(request.body.decode('utf-8'))

            # Create a new Course instance
            course = Course(
                instructor_id=data.get('instructor'),  # Assuming 'instructor' is the instructor ID
                title=data.get('title'),
                description=data.get('description'),
                image=data.get('image'),
            )

            # Save the course to the database
            course.save()

            # Return a success response
            return JsonResponse({'message': 'Course added successfully'})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
