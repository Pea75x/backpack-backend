# Generated by Django 4.0.6 on 2022-07-15 13:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bag', '0008_remove_order_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]