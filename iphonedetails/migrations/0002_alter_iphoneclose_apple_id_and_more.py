# Generated by Django 4.1.9 on 2023-06-25 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iphonedetails', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iphoneclose',
            name='Apple_ID',
            field=models.CharField(blank=True, default='Empty', max_length=100),
        ),
        migrations.AlterField(
            model_name='iphoneclose',
            name='password',
            field=models.CharField(blank=True, default='Empty', max_length=100),
        ),
    ]
