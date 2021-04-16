from django.contrib.auth.models import User
from django.db import models


class Poll(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField(auto_now_add=True)
    finish_date = models.DateField()
    descriptions = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Choice(models.Model):
    answer_type_choice = (
        ('1', 'Text'),
        ('2', 'Single choice'),
        ('3', 'Multiple choice'),
    )


class Question(models.Model):
    poll = models.ForeignKey("Poll", on_delete=models.CASCADE)
    type_question = models.CharField(max_length=1, choices=Choice.answer_type_choice)
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.text


class ChoiceType(models.Model):
    question = models.ForeignKey("Question", on_delete=models.CASCADE)
    choice_type = models.CharField(max_length=100)

    def __str__(self):
        return self.choice_type


class Answer(models.Model):
    question = models.ForeignKey("Question", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200)

    def __str__(self):
        return self.answer
