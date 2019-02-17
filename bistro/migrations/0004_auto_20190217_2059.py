# Generated by Django 2.1.4 on 2019-02-17 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bistro', '0003_auto_20190217_2048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
        migrations.AddField(
            model_name='shop',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bistro.Category'),
            preserve_default=False,
        ),
    ]
