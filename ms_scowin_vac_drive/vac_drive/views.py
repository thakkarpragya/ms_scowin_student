from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .models import VaccineDrive, Student, StudentVaccination
from .serializers import VaccineDriveSerializer, StudentSerializer, StudentVaccinationSerializer
from rest_framework.response import Response

# Create your views here.

class VaccinationDrive(ListCreateAPIView):
    queryset = VaccineDrive.objects.all().order_by('-vacdriveDate')
    serializer_class = VaccineDriveSerializer

class VaccinationDriveDetails(RetrieveUpdateDestroyAPIView):
    queryset =VaccineDrive.objects.all()
    serializer_class = VaccineDriveSerializer
    
class Students(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetails(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer    

class StudentsVaccination(ListCreateAPIView):
    queryset = StudentVaccination.objects.all()
    serializer_class = StudentVaccinationSerializer

class StudentsVaccinationDetails(RetrieveUpdateDestroyAPIView):
    queryset = StudentVaccination.objects.all()
    serializer_class = StudentVaccinationSerializer
    
class VaccinationMetadata(ListAPIView):
    def list(self, request, *args, **kwargs):
        
        #studentCount = 0
        vaccinatedStudentCount = StudentVaccination.objects.all().count()
        upcomingVaccinationDrive = VaccineDrive.objects.filter(driveStatus='Upcoming').values()

        out = {               
            'vaccinatedStudentCount': vaccinatedStudentCount,
            'upcomingVaccinationDrive': upcomingVaccinationDrive,
        }
        return Response(out)        

    
    
