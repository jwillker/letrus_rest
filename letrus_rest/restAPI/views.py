from django.shortcuts import render

from rest_framework.views import APIView, Response
# Create your views here.
from django.shortcuts import render
 
from rest_framework import viewsets
from .models import University, Student
from .serializers import UniversitySerializer, StudentSerializer
 
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
 
class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

 
class CustomView(APIView):
    def get(self, request, format=None):
        return Response("Resposta prod para GET, ex")
 
    def post(self, request, format=None):
        return Response("Resposta prod para POST")