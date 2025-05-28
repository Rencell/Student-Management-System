
from rest_framework import serializers
from .models import Grade

class GradeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'
        