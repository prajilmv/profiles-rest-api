# Generated by Django 2.2 on 2020-04-26 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0013_remove_emptable_emp_dept'),
    ]

    operations = [
        migrations.AddField(
            model_name='emptable',
            name='emp_dept',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='profiles_api.DeptTable'),
        ),
    ]
