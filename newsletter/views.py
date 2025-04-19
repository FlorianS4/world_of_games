from django.shortcuts import render
from django.contrib import messages
from .forms import NewsletterForm


def newsletter(request):
    """
    User can get subscribe to the newsletter
    """

    if request.method == "POST":
        newsletter_form = NewsletterForm(data=request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            messages.add_message(request, messages.SUCCESS,
            "Great Work! You are now subscribed to our newsletter")
        else:
            newsletter_form = NewsletterForm()
            messages.warning(request, 'Your Subscription was not sent. Fill data in correctly. Please try again.')
    newsletter_form = NewsletterForm()

    return render(
        request,
        "newsletter/newsletter.html",
        {
           "newsletter_form": newsletter_form,
        }
    )