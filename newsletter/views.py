from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .forms import NewsletterForm
from profiles.models import UserProfile


def _send_confirmation_email(request):
    """
    Send the user a confirmation email for newsletter
    """
    email = request.POST.get('email')
    subject = render_to_string(
        'newsletter/confirmation_emails/confirmation_email_subject.txt',
        )
    body = render_to_string(
        'newsletter/confirmation_emails/confirmation_email_body.txt',
        {'contact_email': settings.DEFAULT_FROM_EMAIL})

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [email]
    )


def newsletter(request):
    """
    User can get subscribe to the newsletter
    Send email with "confirmation_emails"
    Reused from Checkout app
    """
    success_message = 'Thanks for subscribing to our newsletter! '\
        'We have sent an email to your address. '\
        'We will send newsletters shortly.'

    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            newsletter_form = NewsletterForm(initial={
                'email': profile.user.email,
            })
        except UserProfile.DoesNotExist:
            newsletter_form = NewsletterForm()
    else:
        newsletter_form = NewsletterForm()

    # User submit POST
    if request.method == 'POST':
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            _send_confirmation_email(request)
            messages.success(request, success_message)
            return redirect('home')

    context = {
            "newsletter_form": newsletter_form,
    }
    return render(request, "newsletter/newsletter.html", context)
