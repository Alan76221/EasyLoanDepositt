# Generated by Django 2.2.5 on 2020-08-27 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0002_auto_20190922_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippetnew',
            name='black_check_number',
            field=models.IntegerField(default=1, max_length=100),
        ),
    ]
