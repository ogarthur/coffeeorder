# Generated by Django 2.1.7 on 2019-03-01 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0003_auto_20190228_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='usergroup',
            name='fav',
            field=models.BooleanField(default=False),
        ),
    ]
