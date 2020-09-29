from django.shortcuts import render, redirect
from django.http import HttpResponse
from mainportal.models import home
from mainportal.forms import homeform

# Create your views here.
def mainportal(request):
    if request.method == "POST":
        job_id = request.POST.get('job_id')
        report_no = request.POST.get('report_no')
        name_of_customer = request.POST.get('name_of_customer')
        discipline = request.POST.get('discipline')
        date = request.POST.get('date')
        letter = request.POST.get('letter')
        sample_type = request.POST.get('sample_type')
        
        address_of_customer = request.POST.get('address_of_customer')
        agreement_number = request.POST.get('agreement_number')
        reference_number = request.POST.get('reference_number')
        name_of_work = request.POST.get('name_of_work')
        name_of_agency = request.POST.get('name_of_agency')
        
        group = request.POST.get('group')
        make = request.POST.get('make')

        form = home.objects.create(job_id=job_id, report_no=report_no,  sample_type=sample_type, letter=letter,date=date, address_of_customer=address_of_customer, agreement_number= agreement_number, reference_number= reference_number, name_of_work= name_of_work, group=group, make= make, discipline= discipline, name_of_customer= name_of_customer, name_of_agency= name_of_agency)
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

  