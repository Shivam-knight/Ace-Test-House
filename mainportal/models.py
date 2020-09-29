from django.db import models


# Create your models here.
class home(models.Model):
    options_sample = [
        ("CHEMICAL", 'Chemical'),
        ("MECHANICAL", 'Mechanical'),
        ("BOTH", 'Both'),
    ]
    job_id = models.CharField(max_length=15)
    report_no = models.CharField(max_length=18, unique=True)
    sample_type = models.CharField(max_length=150,null=True )
    
    name_of_customer = models.CharField(max_length=150,null=True )
    address_of_customer = models.CharField(max_length=150, null=True )
    agreement_number = models.CharField(max_length=150, null=True )
    reference_number = models.CharField(max_length=150, null=True )
    name_of_work = models.CharField(max_length=150, null=True )
    name_of_agency = models.CharField(max_length=150, null=True )
    date = models.DateField(null=True, blank=True)
    letter = models.FileField(null=True)
    
    

    discipline = models.CharField(max_length=150,default="",choices=options_sample)
    group = models.CharField(max_length=150, null=True )
    make = models.CharField(max_length=150, null=True )


    def __str__(self):
        return self.job_id