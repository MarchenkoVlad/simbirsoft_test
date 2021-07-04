from django.db import models
from django.conf import settings


class Question(models.Model):
    text = models.TextField('Текст вопроса')

    def __str__(self):
        return self.text


class Choice(models.Model):
    text = models.CharField('Текст ответа', max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField()

    def __str__(self):
        return self.text


class Answer(models.Model):
    user_id = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
