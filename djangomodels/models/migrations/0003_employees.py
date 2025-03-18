# Generated by Django 5.1.7 on 2025-03-12 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('id_number', models.CharField(max_length=50)),
                ('time_in', models.TimeField()),
                ('time_out', models.TimeField()),
                ('hours', models.IntegerField()),
            ],
        ),
    ]
