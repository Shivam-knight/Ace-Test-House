
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('mainportal.urls') ),
    path('account/',include('users_app.urls')),
    
]
