# Generated by Django 4.2.1 on 2023-05-20 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMS_app', '0006_rename_department_team_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeproduct',
            name='status',
            field=models.CharField(max_length=100, null=True),
        ),
    ]