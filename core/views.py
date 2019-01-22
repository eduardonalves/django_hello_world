from django.shortcuts import render

from django.http import HttpResponse


def index(request):
	return render(request,'home.html',{'usuario':'Eduardo Alves'})

def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def contact(request):
    return render(request,'contact.html')    
