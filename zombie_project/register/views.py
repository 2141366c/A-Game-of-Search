from django.shortcuts import render


def index(request):
    return render(request, 'register/login_page.html')

# Create your views here.
