# Generated by Django 2.2.4 on 2019-09-22 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(default='', max_length=100)),
                ('loan', models.CharField(choices=[('one', '$1000'), ('two', '$2000'), ('three', '$3000'), ('four', '$4000'), ('five', '$5000'), ('six', '$6000'), ('seven', '$7000'), ('eight', '$8000')], default='one', max_length=100)),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.IntegerField(default='', max_length=100)),
            ],
        ),
    ]
