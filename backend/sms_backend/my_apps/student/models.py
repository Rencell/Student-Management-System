from django.db import models
from my_apps.subject.models import Subject

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Enrollment
    
    subject = models.ManyToManyField(Subject, through="Enrollment", related_name='student')

    def __str__(self):
        return f"{self.name} ({self.student_number})"
    
    
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) 
    
    class Meta:
        db_table = 'enrollment'
        
    def __str__(self):
        return f"{self.student}"
    

