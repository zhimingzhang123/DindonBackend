# Generated by Django 2.2.1 on 2019-05-05 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dishes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='dishAddTime',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='菜品添加时间'),
        ),
    ]
