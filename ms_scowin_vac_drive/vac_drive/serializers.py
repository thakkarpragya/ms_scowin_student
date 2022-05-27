from rest_framework import serializers 
from .models import VaccineDrive, Student, StudentVaccination

class VaccineDriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaccineDrive
        fields = (            
            'vacdriveDate',
            'vaccineName',
            'dosesAvailable',
            'slots',
            'driveApproval',
            'driveStatus'
        )
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (            
            'id',
            'studentName',
            'dob',
            'gender',
            'aadharID',
            'existingComorbidites'       
        )
        
class StudentVaccinationSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    vaccineDr = VaccineDriveSerializer()
    class Meta:
        model = StudentVaccination
        fields = (
            'id',
            'vaccinationDate',
            'dosage',
            'vaccinationStatus',
            'student',
            'vaccineDr'
        )        
        
        
        
        
      
        
        
         
                
        
        
        
        
        
       