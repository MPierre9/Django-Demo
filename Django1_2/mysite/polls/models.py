from django.db import models
import datetime

from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        # call example: q.was_published_recently will return a boolean
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Employee(models.Model):
    employee_name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)

    hire_date = models.DateTimeField('Hire Date')
    def __str__(self):
        return self.employee_name

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

