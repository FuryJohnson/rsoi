from rest_framework import serializers
from apps.core.models import University, Student, Faculty

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = University

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Student

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Faculty
