# Generated by Django 3.2 on 2021-05-16 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tags', '0013_auto_20210516_1949'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tagrequest',
            old_name='tr_loc',
            new_name='tr_c',
        ),
        migrations.AddField(
            model_name='tagrequest',
            name='tr_p',
            field=models.CharField(default=0, max_length=40),
        ),
        migrations.AddField(
            model_name='tagrequest',
            name='tr_s',
            field=models.CharField(default=0, max_length=40),
        ),
    ]