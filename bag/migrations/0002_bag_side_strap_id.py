# Generated by Django 4.0.6 on 2022-07-13 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('bag', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bag',
            name='side_strap_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='side_strap', to='products.product'),
        ),
    ]