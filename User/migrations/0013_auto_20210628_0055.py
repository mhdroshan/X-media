# Generated by Django 3.2 on 2021-06-27 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0012_following'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='following',
            name='followed',
        ),
        migrations.AddField(
            model_name='following',
            name='is_follow',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='following',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='User.usermodel', verbose_name='UserModel'),
        ),
    ]
