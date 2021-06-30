# Generated by Django 3.0.8 on 2021-06-28 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonInfo',
            fields=[
                ('id', models.AutoField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('major', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=5)),
                ('number', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': '人员信息',
            },
        ),
    ]