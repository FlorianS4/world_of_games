from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib import messages
from .models import AboutUs
from .forms import ContactUsForm


def about_us(request):
    """
    Renders the About us page and contact form
    """
    about_description = AboutUs.objects.all().order_by('-created_on').first()
    if request.method == "POST":
        contact_form = ContactUsForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                request, messages.SUCCESS, "Hey, thanks for your message."
                + " I will check it out and contact you in the next 3 days.")
            return HttpResponseRedirect(reverse('home'))
        else:
            contact_form = ContactUsForm()
            messages.warning(
                request,
                'Your message was not sent. Fill data in correctly. '
                + 'Please try again.')
    contact_form = ContactUsForm()

    return render(
        request,
        "about_us/about_us.html",
        {
            "about_description": about_description,
            "contact_form": contact_form
            },
    )
