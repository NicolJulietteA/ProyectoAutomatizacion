# Generated by Django 3.2.3 on 2021-06-01 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('ccod', models.AutoField(primary_key=True, serialize=False)),
                ('cfechac', models.DateField()),
                ('cnombre', models.CharField(max_length=25)),
                ('cnfiscal', models.IntegerField(max_length=30)),
                ('cdcfiscal', models.CharField(max_length=35)),
                ('cdcdespacho', models.CharField(max_length=30)),
                ('climite', models.IntegerField(max_length=30)),
            ],
        ),
    ]
