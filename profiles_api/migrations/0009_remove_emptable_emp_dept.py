# Generated by Django 2.2 on 2020-04-26 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0008_auto_20200426_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emptable',
            name='emp_dept',
        ),
    ]
