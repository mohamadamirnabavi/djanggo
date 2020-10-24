from django.shortcuts import render
from django.shortcuts import HttpResponse

def home(request):
    # return HttpResponse('test home')
    return render(request,'home.html')

def about(request):
    # return HttpResponse('test about')
    return render(request, 'about.html')
