# Generated by Django 3.2.4 on 2021-06-24 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0002_auto_20210624_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='rollno',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]