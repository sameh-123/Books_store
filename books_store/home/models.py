from django.db import models

# Create your models here.

class book(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class student(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=8)
    def __str__(self):
        return self.username

class Borrow(models.Model):
    student = models.ForeignKey(student, on_delete=models.CASCADE)
    book = models.ForeignKey(book, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateTimeField()

    