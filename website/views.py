from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from website.models import Contact
from website.forms import NameForm, ContactForm, NewsletterForm
from django.contrib import messages


def index_view(request):
    return render(request, 'webtemp/index.html')

def about_view(request):
    return render(request, 'webtemp/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your message has been sent successfully.')
        else:
            messages.add_message(request, messages.ERROR, 'There is an error.Try again later.')

    form = ContactForm()
    return render(request, 'webtemp/contact.html', {'form':form})

def test_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('DONE!')
        else:
            return HttpResponse('NOT VALID!!!')

    form = ContactForm()
    return render(request, 'test.html', {'form':form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')