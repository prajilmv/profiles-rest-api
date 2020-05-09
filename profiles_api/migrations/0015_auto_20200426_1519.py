# Generated by Django 2.2 on 2020-04-26 15:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0014_emptable_emp_dept'),
    ]

    operations = [
        migrations.AddField(
            model_name='depttable',
            name='dept_id',
            field=models.IntegerField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='depttable',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]