from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mainportal(request):
    return render(request, 'mainportal.html',{})