# Generated by Django 3.2 on 2021-06-12 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tags', '0017_auto_20210603_0042'),
    ]

    operations = [
        migrations.AddField(
            model_name='tagrequest',
            name='tr_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]