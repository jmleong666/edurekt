<<<<<<< HEAD
# Generated by Django 3.1.1 on 2020-09-12 07:09
=======
# Generated by Django 3.1 on 2020-08-30 10:54
>>>>>>> d61ab13ba1f64fc7524107bc5835ffe2f2cafbb9

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
<<<<<<< HEAD
                ('code', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('exam_time', models.DateTimeField(blank=True)),
=======
                ('code', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('time', models.DateTimeField(blank=True)),
>>>>>>> d61ab13ba1f64fc7524107bc5835ffe2f2cafbb9
            ],
        ),
    ]
