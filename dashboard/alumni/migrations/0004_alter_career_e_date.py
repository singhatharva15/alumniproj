# Generated by Django 4.0.4 on 2022-05-28 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0003_career_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='e_date',
            field=models.DateField(),
        ),
    ]