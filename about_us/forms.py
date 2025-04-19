from django import forms
from .models import AboutUs, ContactUs


class ContactUsForm(forms.ModelForm):
    """
    Contact Us Form
    """
    class Meta: 
        model = ContactUs
        fields = ('name', 'email', 'contact_description')