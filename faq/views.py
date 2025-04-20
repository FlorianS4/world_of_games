from django.shortcuts import render
from .models import FAQ

# Create your views here.


def faq(request):
    """View to display FAQs"""

    faqs = FAQ.objects.all()
    context = {
        'faqs': faqs,
        }

    return render(request, 'faq/faq.html', context)
