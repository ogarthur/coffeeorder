# Generated by Django 2.1.7 on 2019-05-23 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergroup',
            name='group_color',
            field=models.CharField(default='yellow', max_length=100),
        ),
    ]