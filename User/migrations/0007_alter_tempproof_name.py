# Generated by Django 3.2 on 2021-06-06 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0006_tempproof_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempproof',
            name='name',
            field=models.CharField(default=0, max_length=30, null=True),
        ),
    ]
