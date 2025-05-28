
from rest_framework import  viewsets
from .models import Grade
from .serializer import GradeSerializer

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer