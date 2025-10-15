from django.db import models

# Create your models here.
class student(models.Model):
    student_name = models.CharField(max_length=100)
    student_age = models.IntegerField()
    student_email = models.EmailField()
    student_join = models.DateTimeField(auto_now_add=True)
    student_reg_num = models.IntegerField()

    
