
from rest_framework import serializers
from .models import Grade,GradeType
from my_apps.student.models import Enrollment
from my_apps.student.serializer import EnrollmentSerializer

class GradeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradeType
        fields = '__all__'
class GradeSerializer(serializers.ModelSerializer):
    percentage = serializers.SerializerMethodField()
    enrollment = EnrollmentSerializer(source='enrollment_id', read_only=True)
    enrollment_id = serializers.PrimaryKeyRelatedField(queryset=Enrollment.objects.all())
    class Meta:
        model = Grade
        fields = '__all__'
    
    def get_percentage(self, obj):
        if obj.max_score == 0:
            return 0
        return round((obj.score / obj.max_score) * 100, 2)
    
        