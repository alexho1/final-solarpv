from django.shortcuts import render
from .models import Certificate


# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')


def login(request):
    return render(request, 'myapp/login.html')


def register(request):
    return render(request, 'myapp/registration.html')


def search(request):
    return render(request, 'myapp/search.html')


def search_number(request, number=None):
    cert_list = Certificate.objects.filter(number__contains=number)
    context = {'number': number, 'cert_list': cert_list}
    return render(request, 'myapp/search.html', context)


def search_certificate(request, title=None):
    cert_list = Certificate.objects.filter(title__icontains=title)
    context = {'title': title, 'cert_list': cert_list}
    return render(request, 'myapp/search.html', context)
