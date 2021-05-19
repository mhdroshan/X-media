# Generated by Django 3.2 on 2021-05-11 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_image', models.ImageField(upload_to='post_images')),
                ('p_dateTime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]