from django.urls import path
from first_app import views

urlpatterns = [
    path('users/', views.users, name='users'),
]
