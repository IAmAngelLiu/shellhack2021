# Generated by Django 3.1.2 on 2021-09-25 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('gender', models.CharField(max_length=100, null=True)),
                ('race', models.CharField(max_length=100, null=True)),
                ('firstcollege', models.CharField(max_length=100, null=True)),
                ('data_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
