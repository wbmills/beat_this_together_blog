# Generated by Django 4.1.7 on 2023-10-12 15:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_alter_usefullinks_last_updated_videos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='mod_date',
            field=models.DateField(default=datetime.date(2023, 10, 12)),
        ),
        migrations.AlterField(
            model_name='usefullinks',
            name='last_updated',
            field=models.DateField(default=datetime.datetime(2023, 10, 12, 15, 21, 50, 767680, tzinfo=datetime.timezone.utc)),
        ),
    ]