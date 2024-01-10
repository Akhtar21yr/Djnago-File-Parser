from django.db import models

# Create your models here.
class Student(models.Model):
    rollno = models.IntegerField()
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.BigIntegerField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

class StuAditionalInfo(models.Model):
    rel_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    father_name = models.CharField(max_length=50)
    father_age = models.IntegerField()
    father_phone = models.BigIntegerField()
    father_email = models.EmailField()


