# Generated by Django 2.2 on 2020-04-26 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0011_auto_20200426_1508'),
    ]

    operations = [
        migrations.RenameField(
            model_name='depttable',
            old_name='dept_id',
            new_name='id',
        ),
        migrations.AlterField(
            model_name='emptable',
            name='emp_dept',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='profiles_api.DeptTable', to_field='dept_id'),
        ),
    ]
