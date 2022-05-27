from django.db import models

# Create your models here.

class VaccineDrive(models.Model):
    """
    Vaccination Drive model added here
    """
    vacdriveDate = models.DateTimeField()
    #vacdriveDate = models.DateField()
    vaccineName = models.CharField(max_length=32)
    slots = models.PositiveIntegerField(default=10)
    dosesAvailable = models.PositiveIntegerField(default=100)               
    driveApproval = models.CharField(max_length=32)      
    driveStatus = models.CharField(max_length=32)

    class Meta:
        """
        To override the database table name, use the db_table parameter in class Meta.
        """

    def __str__(self):
        return "{}".format(self.vaccineName)
        
class Student(models.Model):
    """
    Student Vaccination model added here
    """
    id = models.CharField(primary_key=True, max_length=4)
    studentName = models.CharField(max_length=32)
    dob = models.DateTimeField()
    #dob = models.DateField()
    gender = models.CharField(max_length=32)    
    aadharID = models.CharField(max_length=12)
    existingComorbidites = models.CharField(max_length=300, null=True, blank=True)    	 
    
    class Meta:
        """
        To override the database table name, use the db_table parameter in class Meta.
        """

    def __str__(self):
        return "{}".format(self.studentName)  
        
class StudentVaccination(models.Model):
    """
    Student model added here
    """
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    vaccinationDate = models.DateTimeField()
    #vaccinationDate = models.DateField()
    dosage = models.PositiveIntegerField(default=1)
    vaccinationStatus = models.CharField(max_length=32)
    vaccineDr = models.ForeignKey(VaccineDrive, on_delete=models.DO_NOTHING)

    class Meta:
        """
        To override the database table name, use the db_table parameter in class Meta.
        """

    def __str__(self):
        return "{}".format(self.student)        
        



    
     