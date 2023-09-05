from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    path('add', views.add_enrollment, name='add-enrollment'),
    path('enrollments/<int:user_id>/', views.get_user_enrollments, name='get-user-enrollments'),
]
