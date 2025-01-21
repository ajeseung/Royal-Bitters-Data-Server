# Generated by Django 5.1.4 on 2025-01-14 03:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('alcohol', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carts', to='account.account')),
                ('alcohol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_entries', to='alcohol.alcohol')),
            ],
            options={
                'db_table': 'cart',
            },
        ),
    ]
