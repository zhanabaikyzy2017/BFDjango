# Generated by Django 3.0.5 on 2020-04-16 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_category_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.IntegerField(choices=[(1, 'in_warehouse'), (2, 'in_store'), (3, 'sold_out')], default=2),
        ),
    ]
