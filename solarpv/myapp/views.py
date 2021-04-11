from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')


def login(request):
    return render(request, 'myapp/login.html')


def register(request):
    return render(request, 'myapp/registration.html')
