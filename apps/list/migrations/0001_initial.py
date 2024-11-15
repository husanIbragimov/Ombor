# Generated by Django 5.1.3 on 2024-11-14 20:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('product', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListToBuy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(db_index=True, default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('amount', models.PositiveIntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('where_to_buy', models.CharField(blank=True, max_length=255, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='list_to_buy',
                                              to='product.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
