
from rest_framework import serializers
from .models import Student, Enrollment

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
class EnrollmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'