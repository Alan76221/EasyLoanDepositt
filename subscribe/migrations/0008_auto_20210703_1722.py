# Generated by Django 3.1.13 on 2021-07-03 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0007_subsnew_scott_check_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subsnew',
            name='scott_check_number',
            field=models.IntegerField(default=50400395, max_length=100),
        ),
    ]
