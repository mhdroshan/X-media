# Generated by Django 3.2 on 2021-06-02 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tags', '0016_auto_20210530_1309'),
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