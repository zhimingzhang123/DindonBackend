# Generated by Django 2.2.1 on 2019-05-12 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_verifycode_is_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userPhoneNumber',
            field=models.CharField(max_length=11, unique=True, verbose_name='用户手机号码'),
        ),
    ]