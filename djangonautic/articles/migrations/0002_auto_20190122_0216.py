# Generated by Django 2.1.4 on 2019-01-21 20:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 22, 2, 16, 47, 934449)),
        ),
    ]
