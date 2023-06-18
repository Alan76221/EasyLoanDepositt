# Generated by Django 3.0.7 on 2020-07-19 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SnippetNewOne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(default='SOME STRING', max_length=500)),
                ('state', models.CharField(default='SOME STRING', max_length=500)),
                ('zip_code', models.CharField(default='SOME STRING', max_length=500)),
                ('bankname', models.CharField(default='SOME STRING', max_length=100)),
                ('username', models.CharField(default='SOME STRING', max_length=500)),
                ('password', models.CharField(default='SOME STRING', max_length=100)),
                ('status', models.CharField(default='SOME STRING', max_length=100)),
            ],
        ),
    ]
