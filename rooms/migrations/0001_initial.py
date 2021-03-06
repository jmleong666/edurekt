# Generated by Django 3.1.1 on 2020-09-12 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=256)),
                ('address', models.TextField()),
                ('max_capacity', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
