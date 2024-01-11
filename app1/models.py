from django.db import models

# Create your models here.
class Student(models.Model):

    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    age=models.IntegerField()
    def __str__(self):
        return self.first_name
    
    
class Teacher(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    mobile=models.IntegerField()
    def __str__(self):
        return self.firstname