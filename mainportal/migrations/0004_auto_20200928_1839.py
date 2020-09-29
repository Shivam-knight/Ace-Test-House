# Generated by Django 3.1 on 2020-09-28 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainportal', '0003_auto_20200928_0503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='client_info',
        ),
        migrations.AddField(
            model_name='home',
            name='address_of_customer',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='agreement_number',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='discipline',
            field=models.CharField(choices=[('CHEMICAL', 'Chemical'), ('MECHANICAL', 'Mechanical'), ('BOTH', 'Both')], default='', max_length=150),
        ),
        migrations.AddField(
            model_name='home',
            name='group',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='make',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='name_of_agency',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='name_of_customer',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='name_of_work',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='reference_number',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='report_no',
            field=models.CharField(max_length=18, unique=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='sample_type',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
