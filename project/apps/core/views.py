from rest_framework import generics,  permissions
from apps.core.models import University, Student, Faculty
from apps.core.serializers import UniversitySerializer, StudentSerializer, FacultySerializer

class StudentViewSet(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class UniversityViewSet(generics.ListCreateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

class FacultyViewSet(generics.ListCreateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer

