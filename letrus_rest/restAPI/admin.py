from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import University, Student
 
admin.site.register(University)
admin.site.register(Student)