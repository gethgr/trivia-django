from django.db import models

# Create your models here.

class Question(models.Model):
    type = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200, null=True)
    option2 = models.CharField(max_length=200, null=True)
    option3 = models.CharField(max_length=200, null=True)
    option4 = models.CharField(max_length=200, null=True)
    correct_answer = models.CharField(max_length=200)
    def __str__(self):
        return self.question