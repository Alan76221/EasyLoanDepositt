# Generated by Django 3.0.7 on 2020-07-19 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fullcheckinfo', '0003_auto_20200720_0456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankverificationform',
            name='state',
        ),
    ]
