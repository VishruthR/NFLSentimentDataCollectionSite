# Generated by Django 3.2.5 on 2022-07-26 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Count',
            fields=[
                ('counter', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('count_num', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'count',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tweets',
            fields=[
                ('index', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('player', models.TextField(blank=True, null=True)),
                ('tweet', models.TextField(blank=True, null=True)),
                ('score', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tweets',
                'managed': False,
            },
        ),
    ]
