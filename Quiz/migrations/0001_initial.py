# Generated by Django 3.2.4 on 2021-06-24 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('code', models.CharField(max_length=5)),
                ('subject', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('code', models.CharField(max_length=5)),
                ('subject', models.CharField(max_length=30)),
                ('mark', models.CharField(max_length=30)),
            ],
        ),
    ]
