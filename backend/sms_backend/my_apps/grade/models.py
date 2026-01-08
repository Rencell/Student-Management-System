from django.db import models

from my_apps.student.models import Enrollment
from my_apps.subject.models import Subject

class GradeType (models.Model):
    name = models.CharField(max_length=100)

class Grade (models.Model):
    type = models.ForeignKey(GradeType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    max_score = models.IntegerField(default=0)
    enrollment_id = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True) 
    
    
    