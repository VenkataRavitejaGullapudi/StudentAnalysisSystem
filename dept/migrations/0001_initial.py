# Generated by Django 2.0.6 on 2018-07-09 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teac_id', models.IntegerField()),
                ('sub_name', models.CharField(max_length=30)),
                ('sub_code', models.CharField(max_length=10)),
                ('dept_id', models.CharField(max_length=10)),
                ('year', models.CharField(max_length=10)),
            ],
        ),
    ]
