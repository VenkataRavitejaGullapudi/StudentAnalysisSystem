# Generated by Django 2.0.6 on 2018-06-30 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dept', '0002_subjects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjects',
            name='tech_id',
            field=models.IntegerField(),
        ),
    ]