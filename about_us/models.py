from django.db import models

# Create your models here.


class AboutUs(models.Model):
    """
    About us model.
    """
    title = models.CharField(max_length=70, unique=True)
    description = models.TextField(max_length=1000)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class ContactUs(models.Model):
    """
    Contact us model.
    """

    name = models.CharField(max_length=200)
    email = models.EmailField()
    contact_description = models.TextField(max_length=1000)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Contact {self.contact_description} from {self.name}"