# Generated by Django 3.2.4 on 2021-07-07 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_alter_cart_card_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='card_id',
            new_name='cart_id',
        ),
    ]