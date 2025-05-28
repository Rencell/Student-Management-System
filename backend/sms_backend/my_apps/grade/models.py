from django.db import models
from my_apps.student.models import Enrollment


class GradeType (models.Model):
    name = models.CharField(max_length=100)

class Grade (models.Model):
    type = models.ForeignKey(GradeType, on_delete=models.CASCADE)
    enrollment_id = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True) 