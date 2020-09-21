from django.urls import path
from mainportal import views

urlpatterns = [
    path('', views.mainportal, name= 'mainportal'),
    
]
