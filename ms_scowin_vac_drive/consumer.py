import json
import pika
import django
from sys import path
from os import environ

#path.append('E:\BIT-FSE-Projects\C2-Assignment2\ms_scowin_vac_drive\ms_scowin_vac_drive\settings.py') #Your path to settings.py file
environ.setdefault('DJANGO_SETTINGS_MODULE', 'ms_scowin_vac_drive.settings') 
django.setup()
from vac_drive.models import Student

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', heartbeat=600, blocked_connection_timeout=300))
channel = connection.channel()
channel.queue_declare(queue='vacdrive')

def callback(ch, method, properties, body):
    print("Received in vacdrive...")
    print(body)
    data = json.loads(body)
    print(data)

    if properties.content_type == 'student_created':
        if not isinstance(data,list):
            data = [data]
        for d in data:
            student = Student.objects.create(id=d['id'], studentName=d['studentName'], dob=d['dob'], gender=d['gender'], aadharID=d['aadharID'], existingComorbidites=d['existingComorbidites'])
            student.save()
            print("student created")
            
        #for cnt in range(len(data)):
        # student = Student.objects.create(id=data[cnt]['id'], studentName=data[cnt]['studentName'], dob=data[cnt]['dob'], gender=data[cnt]['gender'], aadharID=data[cnt]['aadharID'], existingComorbidites=data[cnt]['existingComorbidites'])
        # student.save()
        # print("student created")
        
    elif properties.content_type == 'student_updated':       
        student = Student.objects.get(id=data['id'])
        student.studentName = data['studentName']
        student.dob = data['dob']
        student.gender = data['gender']
        student.aadharID = data['aadharID']
        student.existingComorbidites = data['existingComorbidites']
        student.save()
        print("student updated")    
  
channel.basic_consume(queue='vacdrive', on_message_callback=callback, auto_ack=True)
print("Started Consuming...")
channel.start_consuming()



