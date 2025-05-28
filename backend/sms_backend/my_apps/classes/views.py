
from rest_framework import  viewsets
from .models import classes_student, Classes
from .serializer import ClassesSerializer, ClassesStudentSerializer

class ClassesViewSet(viewsets.ModelViewSet):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer

class ClassesStudentViewSet(viewsets.ModelViewSet):
    queryset = classes_student.objects.all()
    serializer_class = ClassesStudentSerializer