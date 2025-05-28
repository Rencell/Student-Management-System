from django.db import models
from my_apps.student.models import Student

class Classes (models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True) 
    students = models.ManyToManyField(Student, through='classes_student', related_name='classes')
    
    def __str__(self):
        return f'{self.name}'
    
class classes_student (models.Model):
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True) 
    
    class Meta:
        db_table = 'classes_student'

    def __str__(self):
        return f'{self.classes} ({self.student.name})'