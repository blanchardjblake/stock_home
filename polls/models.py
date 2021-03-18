from django.db import models
from datetime import timedelta
from django.utils.timezone import now


class Question(models.Model):
    """Question model class.

    Attributes
    ----------
    question_text : string
        Holds the text for the question.
    pub_date : datetime
        Holds the date and time of the question.

    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return now() >= self.pub_date >= now() - timedelta(days=1)


class Choice(models.Model):
    """Choice model class.

    Attributes
    ----------
    question : foreign key
        Holds a reference to the Question class object.
    choice_text : string
        Holds a string that represents a choice.

    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
