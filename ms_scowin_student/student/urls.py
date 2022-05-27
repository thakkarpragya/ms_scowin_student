from django.urls import path
#from django import views
from .views import *

urlpatterns = [
    path('students', Students.as_view()),
    path('students/<int:pk>', StudentsDetails.as_view()),
    path('student-metadata', StudentsMetadata.as_view()),    
]