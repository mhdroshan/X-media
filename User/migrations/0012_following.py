# Generated by Django 3.2 on 2021-06-27 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0011_alter_usermodel_u_pass'),
    ]

    operations = [
        migrations.CreateModel(
            name='following',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followed', models.ManyToManyField(related_name='followed', to='User.UserModel')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='User.usermodel')),
            ],
        ),
    ]
