# Generated by Django 3.2.12 on 2022-03-22 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0011_subsnew_scott_customer_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='subsnew',
            name='cashier2022_check_number',
            field=models.IntegerField(default=2467228, max_length=100),
        ),
    ]
