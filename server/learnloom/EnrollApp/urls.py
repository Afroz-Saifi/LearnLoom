from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    path('add', views.add_enrollment, name='add-enrollment'),
]
