# Generated by Django 3.2 on 2021-06-10 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0008_auto_20210607_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='u_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='u_username',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]
