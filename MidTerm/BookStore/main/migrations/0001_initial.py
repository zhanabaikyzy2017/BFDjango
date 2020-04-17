# Generated by Django 2.2 on 2020-03-02 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookJournalBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('price', models.FloatField(default=0)),
                ('description', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bookjournalbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.BookJournalBase')),
                ('genre', models.IntegerField(choices=[('1', 'Criminal'), ('2', 'Drama'), ('3', 'Mystery')])),
            ],
            bases=('main.bookjournalbase',),
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('bookjournalbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.BookJournalBase')),
                ('type', models.IntegerField(choices=[('1', 'Bullet'), ('2', 'Food'), ('3', 'Travel'), ('4', 'Sport')])),
                ('publisher', models.CharField(max_length=200)),
            ],
            bases=('main.bookjournalbase',),
        ),
    ]
