from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    path('add', views.add_assignment, name='add-assignment'),
]
