# Generated by Django 2.0.2 on 2018-07-01 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180701_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='leaving_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
