
from rest_framework import serializers
from .models import Student, Enrollment
from my_apps.subject.serializer import SubjectSerializer
from my_apps.subject.models import Subject

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
class EnrollmentSerializer(serializers.ModelSerializer):
    
    subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    
    class Meta:
        model = Enrollment
        fields = '__all__'
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['subject'] = SubjectSerializer(instance.subject).data
        rep['student'] = StudentSerializer(instance.student).data
        return rep