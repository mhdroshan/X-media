# Generated by Django 3.2 on 2021-06-06 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_auto_20210513_0601'),
    ]

    operations = [
        migrations.CreateModel(
            name='tempProof',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proof', models.ImageField(upload_to='')),
            ],
        ),
    ]