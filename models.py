from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)

class Submission(models.Model):
    user = models.CharField(max_length=100)
