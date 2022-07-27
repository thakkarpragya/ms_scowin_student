from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response

from .producer import publish

# Create your views here.

class Students(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer  

    #def create(self, request, *args, **kwargs):
    def create(self, request):

        
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        # results = Student.objects.all()
        # output_serializer = StudentSerializer(results, many=True)
        # data = output_serializer.data[:]
        publish('student_created', serializer.data,'vacdrive')
        publish('student_created', serializer.data,'studentcomorb')
        return Response(serializer.data)     
    
class StudentsDetails(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def update(self, request, pk=None):
        product = Student.objects.get(pk=pk)
        serializer = StudentSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('student_updated', serializer.data,'vacdrive')
        publish('student_updated', serializer.data,'studentcomorb')
        return Response(serializer.data)    
    
class StudentsMetadata(ListAPIView):
   def list(self, request, *args, **kwargs):
       studentCount = Student.objects.all().count()      
       return Response(studentCount)       
