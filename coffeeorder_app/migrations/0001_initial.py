# Generated by Django 2.1.7 on 2019-03-13 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bar_name', models.CharField(max_length=100)),
                ('bar_description', models.TextField(blank=True, max_length=500, null=True)),
                ('bar_color', models.CharField(default='yellow', max_length=100)),
                ('bar_official', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Combo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('combo_prize', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(blank=True)),
                ('expiration', models.DateField(blank=True)),
                ('total_prize', models.IntegerField(default=0)),
                ('order_bar', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Bar', to='coffeeorder_app.Bar')),
                ('order_group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='UserGroup', to='account_app.UserGroup')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, unique=True)),
                ('product_color', models.CharField(default='white', max_length=100)),
                ('product_type', models.CharField(choices=[('COMIDA', 'comida'), ('BEBIDA', 'Bebida')], max_length=50)),
                ('product_bar', models.ManyToManyField(related_name='product_bar', to='coffeeorder_app.Bar')),
            ],
        ),
        migrations.CreateModel(
            name='ProductVariation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_variation_name', models.CharField(default='NONE', max_length=300)),
                ('product_variation_product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='variation_product', to='coffeeorder_app.Product')),
            ],
        ),
    ]
