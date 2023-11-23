from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=255 ,default='')
    option_a = models.CharField(max_length=255, default='')  
    option_b = models.CharField(max_length=255,default='')
    option_c = models.CharField(max_length=255,default='')
    option_d = models.CharField(max_length=255,default='')
    correct_answer = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
    allowed_time = models.IntegerField()
