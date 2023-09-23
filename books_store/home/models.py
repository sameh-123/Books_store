from django.db import models

# Create your models here.

class student(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=8)

class book(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    date_start=models.DateField()
    student_have=models.ForeignKey(student,on_delete=callable,null=True)
    