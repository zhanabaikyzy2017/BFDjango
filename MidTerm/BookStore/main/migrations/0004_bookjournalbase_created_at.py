# Generated by Django 2.2 on 2020-03-02 04:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200302_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookjournalbase',
            name='created_at',
            field=models.TimeField(default=datetime.time),
        ),
    ]
