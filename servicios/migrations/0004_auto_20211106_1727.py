# Generated by Django 2.2.3 on 2021-11-06 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0003_auto_20211104_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
