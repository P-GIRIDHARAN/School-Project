# Generated by Django 5.1.6 on 2025-02-17 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School_app', '0006_rename_marks_student_mark_student_subject_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_model', models.CharField(max_length=20)),
                ('bus_number', models.IntegerField(default=0)),
            ],
        ),
    ]
