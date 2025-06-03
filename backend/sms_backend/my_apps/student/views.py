
from rest_framework import  viewsets
from .models import Student, Enrollment
from my_apps.subject.models import Subject
from .serializer import StudentSerializer, EnrollmentSerializer
from rest_framework.decorators import action
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @action(detail=False, methods=['get'])
    def count(self, request):
        count = Student.objects.count()
        return Response({'count': count})
class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    
    
    def create(self, request, *args, **kwargs):
        student_id = request.data.get('student')
        subject_id = request.data.get('subject')

        if not student_id or not subject_id:
            return Response({"error": "Student and Subject are required."}, status=status.HTTP_400_BAD_REQUEST)

        student = Student.objects.filter(pk=student_id).first()
        subject = Subject.objects.filter(pk=subject_id).first()
        enrollment, created = Enrollment.objects.update_or_create(
            student=student,
            subject=subject
        )

        serializer = self.get_serializer(enrollment)
        status_code = status.HTTP_201_CREATED if created else status.HTTP_200_OK
        return Response(serializer.data, status=status_code)
    
        
    @action(detail=False, methods=['post'])
    def retrieve_student_subject(self, request):
        class InputSerializer(serializers.Serializer):
            student = serializers.IntegerField()
            
        serializerer = InputSerializer(data=request.data)
        
        if serializerer.is_valid():
            student = serializerer.validated_data['student']
            
            Enrolled = Enrollment.objects.filter(student=student)
            serializer = self.get_serializer(Enrolled, many=True)
            
            return Response(serializer.data , status=status.HTTP_200_OK)
        return Response(serializerer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'])
    def retrieve_subject_student(self, request):
        class InputSerializer(serializers.Serializer):
            subject = serializers.IntegerField()
            
        serializerer = InputSerializer(data=request.data)
        
        if serializerer.is_valid():
            subject = serializerer.validated_data['subject']
            
            Enrolled = Enrollment.objects.filter(subject=subject)
            serializer = self.get_serializer(Enrolled, many=True)
            
            return Response(serializer.data , status=status.HTTP_200_OK)
        return Response(serializerer.errors, status=status.HTTP_400_BAD_REQUEST)
  