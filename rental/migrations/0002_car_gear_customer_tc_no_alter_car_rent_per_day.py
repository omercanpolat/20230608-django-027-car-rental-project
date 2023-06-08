# Generated by Django 4.2.1 on 2023-06-08 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='gear',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='TC_No',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='rent_per_day',
            field=models.PositiveIntegerField(),
        ),
    ]
