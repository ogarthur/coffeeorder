# Generated by Django 2.1.7 on 2019-05-20 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coffeeorder_app', '0007_auto_20190520_2147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='prize',
        ),
    ]
