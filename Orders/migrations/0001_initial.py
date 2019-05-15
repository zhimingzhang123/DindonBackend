# Generated by Django 2.2.1 on 2019-05-14 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='订单编号')),
                ('order_script', models.TextField(null=True, verbose_name='订单留言')),
                ('table_ware_num', models.IntegerField(verbose_name='餐具份数')),
            ],
            options={
                'verbose_name': '订单',
                'verbose_name_plural': '订单',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_time', models.DateTimeField(auto_now_add=True, verbose_name='下单时间')),
                ('order_price', models.FloatField(verbose_name='订单金额')),
                ('pay_method', models.IntegerField(choices=[(0, '支付宝'), (1, '微信支付')], verbose_name='支付方式')),
                ('order_pay_time', models.DateTimeField(blank=True, null=True, verbose_name='付款时间')),
                ('order_process_time', models.DateTimeField(blank=True, null=True, verbose_name='处理时间')),
                ('order_finish_time', models.DateTimeField(blank=True, null=True, verbose_name='完成时间')),
                ('order_confirm_time', models.DateTimeField(blank=True, null=True, verbose_name='确认时间')),
                ('order_status', models.IntegerField(choices=[(0, '已取消'), (1, '已下单'), (2, '已支付'), (3, '处理中'), (4, '已完成'), (5, '已确认')], default=1, verbose_name='订单状态')),
                ('check_info', models.TextField(blank=True, null=True, verbose_name='发票信息')),
                ('trade_info', models.TextField(blank=True, null=True, verbose_name='交易信息')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction', to='Orders.Order', verbose_name='订单编号')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_id', models.IntegerField(verbose_name='菜品编号')),
                ('dish_name', models.CharField(max_length=128, verbose_name='菜品名称')),
                ('dish_price', models.FloatField(verbose_name='菜品价格')),
                ('dish_picture', models.TextField(blank=True, null=True, verbose_name='菜品图片')),
                ('dish_description', models.TextField(blank=True, null=True, verbose_name='菜品描述')),
                ('dish_num', models.IntegerField(verbose_name='菜品数量')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_detail', to='Orders.Order', verbose_name='订单编号')),
            ],
            options={
                'verbose_name': '订单详情',
                'verbose_name_plural': '订单详情',
            },
        ),
    ]
