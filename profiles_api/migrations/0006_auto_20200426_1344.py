# Generated by Django 2.2 on 2020-04-26 13:44

from django.db import migrations, models
import profiles_api.validators


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0005_auto_20200426_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depttable',
            name='dept_name',
            field=models.CharField(max_length=255, validators=[profiles_api.validators.validate_alpha]),
        ),
    ]
