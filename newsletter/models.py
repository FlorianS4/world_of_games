from django.db import models
from django.shortcuts import reverse


class Newsletter(models.Model):
    """
    Newsletter model.
    """
    email = models.EmailField()

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('home')
