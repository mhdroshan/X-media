# Generated by Django 3.2 on 2021-05-02 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tags', '0003_auto_20210503_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='tagmodel',
            name='tag_image',
            field=models.ImageField(default=1, upload_to='tag_pics'),
            preserve_default=False,
        ),
    ]
