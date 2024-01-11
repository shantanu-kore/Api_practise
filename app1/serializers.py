from .models import Student
from rest_framework import serializers

class Studentserializer(serializers.Serializer):
    first_name=serializers.CharField(max_length=100)
    last_name=serializers.CharField(max_length=100)
    age=serializers.IntegerField()





    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    def update(self, student, validated_data):
        newstudent=Student(**validated_data)
        newstudent.id=student.id
        newstudent.save()
        return newstudent
    
class Teacherserializer(serializers.Serializer):
    first_name=serializers.CharField(max_length=100)
    last_name=serializers.CharField(max_length=100)
    email=serializers.CharField(max_length=50)
    password=serializers.CharField(max_length=30)
    username=serializers.CharField(max_length=30)
   