# Generated by Django 2.1.7 on 2019-03-11 13:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_auto_20190311_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 11, 13, 35, 28, 302620)),
        ),
    ]
