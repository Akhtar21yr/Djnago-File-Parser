from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import StudentSerializer,StudentInfoSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Student
import openpyxl


# Create your views here.
class Parser(APIView):
    def post(self,request):
        data = request.FILES['student']
        workbook = openpyxl.load_workbook(data)
        sheet = workbook.active

        for row in sheet.iter_rows(min_row = 2,values_only = True):
            rollno,name,age,email,phone,city,state = row
            student = Student(name = name ,age=age,rollno=rollno,email=email,phone=phone,city=city,state=state)
            serializer = StudentSerializer(data=student)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':serializer.data},status=status.HTTP_201_CREATED)
            else :
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
        
        return Response({'msg':'some error occured'})
    
    def get(self,request,id=None):
        if not id :
            try :
                student=Student.objects.all()
                serializer = StudentSerializer(student,many=True)
                return Response({'msg':serializer.data})
            except:
                return Response({'msg':'student not found'},status=status.HTTP_404_NOT_FOUND)
        else :
            student = Student.objects.filter(rollno = id).first()
            serializer = StudentSerializer(student)
            return Response({'msg':serializer.data},status=status.HTTP_200_OK)
        
    
class AdditionInfo(APIView):
    def Post(self,request):
        serializer = StudentSerializer(data=request.data)
        serializer2 = StudentInfoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            if serializer2.is_valid(raise_exception=True):
                serializer2.save()
                return Response({'msg':'creted'},status=status.HTTP_201_CREATED)
        return Response({'msg':'some error occured'})
    
