# Generated by Django 3.2 on 2021-05-02 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tags', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Studentname',
            new_name='Tagmodel',
        ),
        migrations.RenameField(
            model_name='tagmodel',
            old_name='name',
            new_name='tag_name',
        ),
        migrations.RenameField(
            model_name='tagmodel',
            old_name='num',
            new_name='tag_title',
        ),
    ]
