# Generated by Django 2.2.4 on 2019-10-02 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CannedResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('canned_name', models.CharField(max_length=500)),
                ('canned', models.CharField(max_length=100000)),
            ],
        ),
    ]
