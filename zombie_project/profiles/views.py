from django.shortcuts import render
from django.http import HttpResponse
from profiles.models import Player

def index(request):	
	return render(request, 'profiles/index.html')

# def base(request):
    # return render(request, 'profiles/base.html')	

# def status(request):
    # return render(request, 'profiles/status.html')
	
# def badges(request):
    # return render(request, 'profiles/badges.html')


