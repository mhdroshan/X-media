# Generated by Django 3.2 on 2021-05-15 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_auto_20210513_0601'),
        ('Posts', '0004_auto_20210511_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='u_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='User.usermodel', verbose_name='UserModel'),
        ),
    ]
