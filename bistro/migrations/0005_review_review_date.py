# Generated by Django 2.1.4 on 2019-02-18 09:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bistro', '0004_auto_20190217_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='review_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 18, 9, 13, 4, 98804, tzinfo=utc), verbose_name='date published'),
            preserve_default=False,
        ),
    ]
