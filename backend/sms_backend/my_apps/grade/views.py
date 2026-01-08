
from rest_framework import  viewsets
from .models import Grade, GradeType
from .serializer import GradeSerializer, GradeTypeSerializer
from rest_framework.decorators import action
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum, F, FloatField, Value, Case, When,ExpressionWrapper

class GradeViewSet(viewsets.ModelViewSet):
    queryset = GradeType.objects.all()
    serializer_class = GradeTypeSerializer
class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    
    @action(detail=False, methods=['get'])
    def total_percentage(self, request):
        total_percentage = Grade.objects.aggregate(
            total_score=Sum('score'),
            total_max=Sum('max_score')
        )
        total_score = total_percentage['total_score'] or 0
        total_max = total_percentage['total_max'] or 0
        
        if total_max == 0:
            percentage = 0
        else:
            percentage = round((total_score / total_max) * 100, 2)
        
        
        return Response({'percentage': percentage})
    
    @action(detail=False, methods=['post'])
    def get_student_grade(self, request):
        class InputSerializer(serializers.Serializer):
            enrollment_id = serializers.IntegerField()
        
        serializerer = InputSerializer(data=request.data)

        if serializerer.is_valid():
            enrollment_id = serializerer.validated_data['enrollment_id']
            
            Enrolled = Grade.objects.filter(enrollment_id=enrollment_id)
            serializer = self.get_serializer(Enrolled, many=True)
            
            return Response(serializer.data , status=status.HTTP_200_OK)
        return Response(serializerer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'])
    def get_grade_type(self, request):
        grade_types = GradeType.objects.all()
        serializer = GradeTypeSerializer(grade_types, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'], url_path='get-grade-average')
    def get_grade_average(self, request):
        enrollment_id = request.query_params.get('enrollment_id')
        
        if not enrollment_id:
            return Response({"error": "Missing enrollment_id"}, status=400)
        
        def grade_type(type):
            filters = {'enrollment_id': enrollment_id}
            
            if(type != 0):
                filters['type'] = type
            
            agg = Grade.objects.filter(**filters).aggregate(
                total_score=Sum('score'),
                total_max=Sum('max_score')
            )
            total_score = agg['total_score'] or 0
            total_max = agg['total_max'] or 0
            
            if total_max == 0:
                return 0
            
            return round((total_score / total_max) * 100, 2)

        return Response({
            'enrollment_id': enrollment_id,
            'average_quiz': grade_type(1),
            'average_assignment': grade_type(2),
            'average_activity': grade_type(3),
            'average_grade': grade_type(0),
        })
        
    @action(detail=False, methods=['get'])
    def get_overall_average(self, request):
        enrollment_id = request.query_params.get('enrollment_id')
        
        if not enrollment_id:
            return Response({"error": "Missing enrollment_id"}, status=400)
    
        agg = Grade.objects.filter(enrollment_id=enrollment_id).aggregate(
            total_score=Sum('score'),
            total_max=Sum('max_score')
        )
        total_score = agg['total_score'] or 0
        total_max = agg['total_max'] or 0
        
        if total_max == 0:
            percentage = 0
        else:
            percentage = round((total_score / total_max) * 100, 2)

        return Response({
            'enrollment_id': enrollment_id,
            'average_grade': percentage,
        })
    
    @action(detail=False, methods=['get'])
    def get_average_by_subject(self, request):
        subject_id = request.query_params.get('subject_id')
        
        if not subject_id:
            return Response({"error": "Missing subject_id"}, status=400)
    
        agg = Grade.objects.filter(subject=subject_id).aggregate(
            total_score=Sum('score'),
            total_max=Sum('max_score')
        )
        total_score = agg['total_score'] or 0
        total_max = agg['total_max'] or 0
        
        if total_max == 0:
            percentage = 0
        else:
            percentage = round((total_score / total_max) * 100, 2)

        return Response({
            'subject': subject_id,
            'average_grade': percentage,
        })
    
    @action(detail=False, methods=['get'])
    def get_average_by_student(self, request, url_path='get_average_by_student'):
        student_id = request.query_params.get('student_id')
        
        grades = (
            Grade.objects
            .values(student_id=F('enrollment_id__student'), student_name=F('enrollment_id__student__name'))
            .annotate(
                total_score=Sum('score'),
                total_max=Sum('max_score'),
                percentage=Case(
                    When(total_max=0, then=Value(0)),
                    default=100.0 * Sum('score') / Sum('max_score'),
                    output_field=FloatField()
                )  
            ).order_by('-percentage')
        )
        return Response({
            'grade': grades,
        })
    
    @action(detail=False, methods=['get'])
    def get_average_by_detail_student(self, request):
        student_id = request.query_params.get('student_id')
        
        if not student_id:
            return Response({"error": "Missing student_id"}, status=400)
    
        agg = Grade.objects.filter(enrollment_id__student=student_id).aggregate(
            total_score=Sum('score'),
            total_max=Sum('max_score')
        )
        total_score = agg['total_score'] or 0
        total_max = agg['total_max'] or 0
        
        if total_max == 0:
            percentage = 0
        else:
            percentage = round((total_score / total_max) * 100, 2)

        return Response({
            'student': student_id,
            'average_grade': percentage,
        })
    
            
        
        
        