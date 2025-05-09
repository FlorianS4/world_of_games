from django import forms
from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    """
    Contact Us Form
    """
    class Meta:
        model = ContactUs
        fields = ('name', 'email', 'contact_description')
