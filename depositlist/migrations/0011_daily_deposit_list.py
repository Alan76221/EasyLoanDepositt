# Generated by Django 4.1.6 on 2023-02-07 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depositlist', '0010_commitment_create'),
    ]

    operations = [
        migrations.CreateModel(
            name='Daily_Deposit_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('full_name', models.CharField(default='Empty', max_length=500)),
                ('email', models.CharField(default='Empty', max_length=500)),
                ('phone', models.CharField(default='Empty', max_length=500)),
                ('bank_name', models.CharField(default='Empty', max_length=500)),
                ('username', models.CharField(default='Empty', max_length=500)),
                ('password', models.CharField(default='Empty', max_length=500)),
                ('special_notice', models.CharField(default='Empty', max_length=2000)),
                ('ultimate_form_id', models.CharField(default='Test', max_length=2000)),
            ],
        ),
    ]
