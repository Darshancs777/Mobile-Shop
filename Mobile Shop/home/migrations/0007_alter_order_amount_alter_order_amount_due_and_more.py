# Generated by Django 5.0.7 on 2024-08-14 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_order_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='amount_due',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='amount_paid',
            field=models.FloatField(default=0),
        ),
    ]
