from django import forms
from .models import FAQ


class FAQForm(forms.ModelForm):
    """
    FAQ Form
    """

    class Meta:
        model = FAQ
        fields = ['question', 'answer']
