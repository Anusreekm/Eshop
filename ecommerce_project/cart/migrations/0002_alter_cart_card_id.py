# Generated by Django 3.2.4 on 2021-07-07 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='card_id',
            field=models.IntegerField(),
        ),
    ]
