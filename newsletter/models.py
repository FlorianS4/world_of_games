from django.db import models


class Newsletter(models.Model):
    """
    Newsletter model.
    """
    email = models.EmailField()

    def __str__(self):
        return self.email
