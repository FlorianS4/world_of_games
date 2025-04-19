from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import AboutUs


class AboutUsForm(forms.ModelForm):
    description = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = AboutUs
