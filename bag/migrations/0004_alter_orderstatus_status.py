# Generated by Django 4.0.6 on 2022-07-14 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bag', '0003_alter_orderstatus_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderstatus',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('confirmed', 'confirmed'), ('making', 'making'), ('created', 'created'), ('dispatched', 'dispatched'), ('delivered', 'delivered')], default='pending', max_length=100),
        ),
    ]