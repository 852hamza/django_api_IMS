# Generated by Django 4.2.1 on 2023-05-17 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMS_app', '0004_alter_product_product_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeedetail',
            name='designation',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employeeproduct',
            name='assign_by',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='manufacture_by',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_capacity',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
