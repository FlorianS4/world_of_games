from django import forms
from .models import Newsletter


class NewsletterForm(forms.ModelForm):
    """
    Newsletter Form
    """
    class Meta:
        model = Newsletter
        fields = ('email',)
