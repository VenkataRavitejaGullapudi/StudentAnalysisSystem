# Generated by Django 2.0.6 on 2018-07-09 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('teac_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('mobile', models.IntegerField()),
                ('dept_id', models.IntegerField()),
            ],
        ),
    ]
