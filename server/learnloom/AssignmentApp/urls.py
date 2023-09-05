from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    path('add', views.add_assignment, name='add-assignment'),
    path('assignments/<int:course_id>/<str:enroll_date>', views.get_assignments_for_course, name='get-assignments-for-course'),
]
