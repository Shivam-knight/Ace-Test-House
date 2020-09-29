from django import forms
from mainportal.models import home

class homeform(forms.ModelForm):
    class Meta:
        model = home
        fields = ['job_id', 'report_no', 'name_of_customer', 'sample_type','letter', 'date']