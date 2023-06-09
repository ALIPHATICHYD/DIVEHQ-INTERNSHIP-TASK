from django.urls import path 
from .import views

urlpatterns=[
    path('users-reg/', views.Register.as_view()),
]