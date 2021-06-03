# Generated by Django 3.2 on 2021-06-03 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_auto_20210513_0601'),
        ('Posts', '0010_auto_20210529_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('com_data', models.TextField()),
                ('com_time', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Posts.postmodel', verbose_name='postmodel')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='User.usermodel', verbose_name='UserModel')),
            ],
        ),
    ]