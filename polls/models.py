from django.db import models

# Think as there are two tables in the model 

class Question(models.Model):
    # this table has two fileds, one is a question text holds 200 char, another is the date
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)