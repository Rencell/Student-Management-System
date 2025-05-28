
from rest_framework import serializers
from .models import classes_student, Classes

class ClassesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Classes
        fields = '__all__'
        
class ClassesStudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = classes_student
        fields = '__all__'