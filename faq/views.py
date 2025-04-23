from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import FAQ
from .forms import FAQForm

# Create your views here.


def faq(request):
    """View to display FAQs"""

    faqs = FAQ.objects.all()

    if request.method == "POST":
        faq_form = FAQForm(data=request.POST)
        if faq_form.is_valid():
            faq_form.save()
            messages.add_message(
                request, messages.SUCCESS, "Thanks for the FAQ")
        else:
            faq_form = FAQForm()
            messages.warning(
                request,
                'Your FAQ was not sent. Fill data in correctly. '
                + 'Please try again.')
    faq_form = FAQForm()

    context = {
        'faqs': faqs,
        'faq_form': faq_form
        }

    return render(request, 'faq/faq.html', context)
