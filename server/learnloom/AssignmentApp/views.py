from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Assignment
from CourseApp.models import Course  # Import the Course model from the CourseApp
from datetime import datetime

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


@csrf_exempt  # Only for development; remove in production and use proper authentication.
def get_assignments_for_course(request, course_id, enroll_date):
    if request.method == 'GET':
        try:
            # Parse the enroll date as a datetime object
            enroll_date = datetime.strptime(enroll_date, '%Y-%m-%d')

            # Retrieve assignments for the course where start_date > enroll_date
            assignments = Assignment.objects.filter(course_id=course_id, start_date__gt=enroll_date)
            assignments_data = []

            for assignment in assignments:
                assignment_data = {
                    'id': assignment.id,
                    'course': assignment.course_id,
                    'start_date': assignment.start_date.strftime('%Y-%m-%d %H:%M:%S'),
                    'end_date': assignment.end_date.strftime('%Y-%m-%d %H:%M:%S'),
                    'title': assignment.title,
                    'description': assignment.description,
                }
                assignments_data.append(assignment_data)

            return JsonResponse(assignments_data, safe=False)

        except ValueError:
            return JsonResponse({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=400)
        except Assignment.DoesNotExist:
            return JsonResponse([], safe=False)

    return JsonResponse({'error': 'Invalid request method'}, status=405)