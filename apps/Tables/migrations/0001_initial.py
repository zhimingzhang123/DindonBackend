# Generated by Django 2.2.1 on 2019-05-05 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiningTable',
            fields=[
                ('tableId', models.AutoField(primary_key=True, serialize=False, verbose_name='餐桌编号')),
                ('tableCategory', models.IntegerField(verbose_name='餐桌类别')),
                ('tableState', models.IntegerField(verbose_name='餐桌状态')),
            ],
        ),
    ]
