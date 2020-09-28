from django.db import models

# Create your models here.
class home(models.Model):
    options_sample = [
        ("CHEMICAL", 'Chemical'),
        ("MECHANICAL", 'Mechanical'),
        ("BOTH", 'Both'),
    ]
    job_id = models.CharField(max_length=15)
    report_no = models.CharField(max_length=18)
    client_info = models.CharField(max_length=100)
    sample_type = models.CharField(max_length=150, choices=options_sample)

    def __str__(self):
        return self.job_id