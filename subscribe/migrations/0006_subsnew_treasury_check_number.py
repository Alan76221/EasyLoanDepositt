# Generated by Django 3.0.10 on 2020-10-13 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0005_auto_20201010_0802'),
    ]

    operations = [
        migrations.AddField(
            model_name='subsnew',
            name='treasury_check_number',
            field=models.IntegerField(default=44355757),
        ),
    ]
