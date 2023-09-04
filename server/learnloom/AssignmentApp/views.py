from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Assignment

@csrf_exempt  # Only for development; remove in production and use proper authentication.
def add_assignment(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from request body
            data = json.loads(request.body.decode('utf-8'))

            # Create a new Assignment instance
            assignment = Assignment(
                course_id=data.get('course'),  # Assuming 'course' is the course ID
                start_date=data.get('start_date'),
                end_date=data.get('end_date'),
                title=data.get('title'),
                description=data.get('description'),
            )

            # Save the assignment to the database
            assignment.save()

            # Return a success response
            return JsonResponse({'message': 'Assignment added successfully'})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
