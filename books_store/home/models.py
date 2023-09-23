from django.db import models

# Create your models here.
class book(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    date_start=models.DateField()
    date_end=models.DateField()
    def __str__(self):
        return self.name
class student(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=8)
    book_have=models.ForeignKey(book,on_delete=callable,null=True)