from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Instructor

@csrf_exempt  # Only for development; remove in production and use proper authentication.
def register_instructor(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from request body
            data = json.loads(request.body.decode('utf-8'))

            # Create a new Instructor instance
            instructor = Instructor(
                username=data.get('username'),
                email=data.get('email'),
                password=data.get('password'),
                role=data.get('role', 'instructor'),  # Default to 'instructor'
            )

            # Save the instructor to the database
            instructor.save()

            # Return a success response
            return JsonResponse({'message': 'Instructor registered successfully'})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
