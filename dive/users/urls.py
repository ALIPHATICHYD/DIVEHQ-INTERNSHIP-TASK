from django.urls import path 
from .import views

urlpatterns=[
    path('users-reg/', views.RegisterUser.as_view()),

]