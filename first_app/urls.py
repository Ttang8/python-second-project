from django.urls import path
from first_app import views

urlpatterns = [
    path('users/', views.users, name='users'),
    path('usersform/',views.usersform,name='usersform'),
    path('', views.index,name='index')
]
