
from rest_framework import  viewsets
from .models import Subject
from .serializer import SubjectSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
