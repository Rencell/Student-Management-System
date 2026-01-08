
from rest_framework import  viewsets
from .models import Subject
from .serializer import SubjectSerializer
from rest_framework.decorators import action
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    
    @action(detail=False, methods=['get'])
    def count(self, request):
        count = Subject.objects.count()
        return Response({'count': count})
