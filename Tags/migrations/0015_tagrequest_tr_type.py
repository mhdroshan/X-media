# Generated by Django 3.2 on 2021-05-30 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tags', '0014_auto_20210516_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='tagrequest',
            name='tr_type',
            field=models.CharField(default=0, max_length=40),
        ),
    ]