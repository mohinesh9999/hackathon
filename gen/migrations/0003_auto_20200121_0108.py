# Generated by Django 2.2.2 on 2020-01-20 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gen', '0002_auto_20200121_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='gender',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='password',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='signup',
            name='verified',
            field=models.CharField(blank=True, default='no', max_length=3, null=True),
        ),
    ]