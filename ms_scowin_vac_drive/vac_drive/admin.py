from django.contrib import admin

# Register your models here.

from .models import VaccineDrive, Student, StudentVaccination

admin.site.register(VaccineDrive)
admin.site.register(Student)
admin.site.register(StudentVaccination)
