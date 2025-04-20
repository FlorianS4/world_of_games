from django.db import models

# Create your models here.


class FAQ(models.Model):
    """
    Model for storing FAQ questions and answers.
    """

    question = models.CharField(max_length=500, null=False, blank=False)
    answer = models.TextField(max_length=2000, null=False, blank=False)

    def __str__(self):
        return self.question
