# Generated by Django 4.0.6 on 2022-07-15 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bag', '0006_remove_order_bag_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='bag',
            name='order_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='item', to='bag.order'),
            preserve_default=False,
        ),
    ]
