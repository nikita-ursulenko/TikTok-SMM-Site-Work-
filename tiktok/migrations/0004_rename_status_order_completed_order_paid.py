# Generated by Django 4.2 on 2023-06-16 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiktok', '0003_order_delete_orderid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='status',
            new_name='completed',
        ),
        migrations.AddField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
