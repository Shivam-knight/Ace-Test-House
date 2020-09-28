from django.shortcuts import render, redirect
from django.http import HttpResponse
from mainportal.models import home
from mainportal.forms import homeform
# Create your views here.
def mainportal(request):
    if request.method == "POST":
        job_id = request.POST.get('job_id')
        report_no = request.POST.get('report_no')
        client_info = request.POST.get('client_info')
        sample_type = request.POST.get('sample_type')
        form = home.objects.create(job_id=job_id, report_no=report_no, client_info=client_info, sample_type=sample_type)
        form.save()
        return redirect('mainportal')
    else:
        all_id = home.objects.all()
        return render(request, 'mainportal.html',{'all_id': all_id})

def reports(request):
    return render(request, 'reports.html',{})

def jobsearch(request):
    return render(request, 'jobsearch.html',{})

def createSample(request):
    return render(request, 'createSample.html',{})      

def attendance(request):
    return render(request, 'attendance.html',{})

def category(request):
    return render(request, 'category.html',{})

  