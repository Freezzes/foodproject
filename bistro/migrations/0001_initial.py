# Generated by Django 2.1.4 on 2019-02-16 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bistro.Shop'),
        ),
    ]
