# Generated by Django 3.2 on 2021-05-14 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tags', '0009_auto_20210515_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tagmodel',
            name='t_country',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='tagmodel',
            name='t_place',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='tagmodel',
            name='t_state',
            field=models.CharField(max_length=20),
        ),
    ]
