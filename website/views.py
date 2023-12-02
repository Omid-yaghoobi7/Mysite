from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from website.models import Contact
from website.forms import NameForm, ContactForm


def index_view(request):
    return render(request, 'webtemp/index.html')

def about_view(request):
    return render(request, 'webtemp/about.html')

def contact_view(request):
    return render(request, 'webtemp/contact.html')

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