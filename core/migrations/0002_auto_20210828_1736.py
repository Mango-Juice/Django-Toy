# Generated by Django 2.2.4 on 2021-08-28 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='create_date',
        ),
        migrations.RemoveField(
            model_name='suggestion',
            name='create_date',
        ),
    ]