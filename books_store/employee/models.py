from django.db import models

# Create your models here.
class adminall(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=8)
    def __str__(self):
        return self.username