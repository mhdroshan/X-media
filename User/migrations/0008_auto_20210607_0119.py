# Generated by Django 3.2 on 2021-06-06 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0007_alter_tempproof_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='u_email',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='u_phone',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
