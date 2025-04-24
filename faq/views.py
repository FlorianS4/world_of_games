from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponseRedirect)
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
            return HttpResponseRedirect(reverse('home'))
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


@login_required
def edit_faq(request, faq_id):
    """
    Edit a faq in the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    faq = get_object_or_404(FAQ, pk=faq_id)
    if request.method == 'POST':
        form = FAQForm(request.POST, request.FILES, instance=faq)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated faq!')
            return redirect(reverse('faq'))
        else:
            messages.error(request,
                           'Failed to update faq. Please ensure the ' +
                           'form is valid.')
    else:
        form = FAQForm(instance=faq)
        messages.info(request, f'You are editing {faq.question}')

    template = 'faq/edit_faq.html'
    context = {
        'form': form,
        'faq': faq,
    }

    return render(request, template, context)


@login_required
def delete_faq(request, faq_id):
    """
    Delete a faq from the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    faq = get_object_or_404(FAQ, pk=faq_id)
    faq.delete()
    messages.success(request, 'FAQ deleted!')
    return redirect(reverse('faq'))
