from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    path('add', views.add_submission, name='add-submission'),
     path('submissions/<int:assignment_id>/', views.get_submissions_by_assignment, name='get-submissions-by-assignment'),
]
