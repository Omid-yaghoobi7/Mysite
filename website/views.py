from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def index_view(request):
    return render(request, 'webtemp/index.html')

def about_view(request):
    return render(request, 'webtemp/about.html')

def contact_view(request):
    return render(request, 'webtemp/contact.html')