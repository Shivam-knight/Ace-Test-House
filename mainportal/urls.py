from django.urls import path
from mainportal import views

urlpatterns = [
    path('', views.mainportal, name= 'mainportal'),
    path('reports', views.reports, name= 'reports'),
    path('jobsearch', views.jobsearch, name= 'jobsearch'),
    path('createSample', views.createSample, name= 'createSample'),
    path('attendance', views.attendance, name= 'attendance'),
    path('category', views.category, name= 'category'),
    
    
]
