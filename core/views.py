from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from .models import Student
from .serializers import StudentSerializer


class StudentAPIv1ViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()