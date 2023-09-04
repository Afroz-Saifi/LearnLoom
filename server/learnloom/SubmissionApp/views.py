from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Submission

@csrf_exempt  # Only for development; remove in production and use proper authentication.
def add_submission(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from request body
            data = json.loads(request.body.decode('utf-8'))

            # Create a new Submission instance
            submission = Submission(
                student_id=data.get('student'),          # Assuming 'student' is the student ID
                assignment_id=data.get('assignment'),    # Assuming 'assignment' is the assignment ID
                submissionLink=data.get('submissionLink'),
                username=data.get('username'),
            )

            # Save the submission to the database
            submission.save()

            # Return a success response
            return JsonResponse({'message': 'Submission added successfully'})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
