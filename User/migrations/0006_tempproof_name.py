# Generated by Django 3.2 on 2021-06-06 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_tempproof'),
    ]

    operations = [
        migrations.AddField(
            model_name='tempproof',
            name='name',
            field=models.CharField(default=0, max_length=30),
        ),
    ]
