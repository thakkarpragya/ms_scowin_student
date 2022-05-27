from django.urls import path
#from django import views
from .views import *

urlpatterns = [
    path('vaccinationdrive', VaccinationDrive.as_view()),
    path('vaccinationdrive/<int:pk>', VaccinationDriveDetails.as_view()),
    path('students', Students.as_view()),
    path('students/<int:pk>', StudentDetails.as_view()),
    path('student-vaccination', StudentsVaccination.as_view()),
    path('student-vaccination/<int:pk>', StudentsVaccinationDetails.as_view()),
    path('vaccination-metadata', VaccinationMetadata.as_view()),
]