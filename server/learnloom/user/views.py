from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User    

@csrf_exempt  # Only for development; remove in production and use proper authentication.
def register_user(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from request body
            data = json.loads(request.body.decode('utf-8'))

            # Create a new User instance
            user = User(
                username=data.get('username'),
                email=data.get('email'),
                password=data.get('password'),
                role=data.get('role', 'student'),  # Default to 'student'
                isenroll=data.get('isenroll', False),  # Default to False
            )

            # Save the user to the database
            user.save()

            # Return a success response
            return JsonResponse({'message': 'User registered successfully'})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

# user login route
@csrf_exempt  # Only for development; remove in production and use proper authentication.
def user_login(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from request body
            data = json.loads(request.body.decode('utf-8'))

            # Retrieve the user by email and password
            user = User.objects.filter(email=data.get('email'), password=data.get('password')).first()

            if user:
                # User exists, return user data
                user_data = {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'role': user.role,
                    'isenroll': user.isenroll,
                }
                return JsonResponse(user_data)
            else:
                return JsonResponse({'error': 'User not found'}, status=404)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)