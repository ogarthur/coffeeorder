# Generated by Django 2.1.7 on 2019-02-22 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BarProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bar_product_prize', models.IntegerField(default=0)),
                ('bar_product_stock', models.BooleanField(default=False)),
                ('bar_product_combo', models.ManyToManyField(related_name='bar_product_combo', to='order_app.Combo')),
                ('bar_product_order_list', models.ManyToManyField(related_name='bar_product_order_list', to='order_app.OrderList')),
            ],
        ),
        migrations.RemoveField(
            model_name='productbar',
            name='product_combo',
        ),
        migrations.RemoveField(
            model_name='productbar',
            name='product_order_list',
        ),
        migrations.DeleteModel(
            name='ProductBar',
        ),
    ]
