# Generated by Django 3.2.4 on 2021-06-24 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0003_student_rollno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='mark',
            field=models.IntegerField(),
        ),
    ]
