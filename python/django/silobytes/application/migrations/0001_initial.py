# Generated by Django 3.1.6 on 2021-02-12 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_change', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                (
                    'email',
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    'phone',
                    models.CharField(blank=True, max_length=20, null=True),
                ),
            ],
            options={'unique_together': {('name', 'phone')}},
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_change', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                (
                    'description',
                    models.CharField(blank=True, max_length=255, null=True),
                ),
            ],
            options={'abstract': False},
        ),
        migrations.CreateModel(
            name='Silo',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_change', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                (
                    'description',
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ('size', models.FloatField()),
            ],
            options={'abstract': False},
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_change', models.DateTimeField(auto_now=True)),
                ('annotations', models.TextField(blank=True, null=True)),
                ('quantity', models.FloatField()),
                ('entry_date', models.DateTimeField()),
                ('withdrawal_date', models.DateTimeField()),
                (
                    'payment_method',
                    models.CharField(
                        blank=True,
                        choices=[
                            ('money', 'Money'),
                            ('credit-card', 'Credit Card'),
                            ('debit-card', 'Debit Card'),
                            ('deposit', 'Deposit'),
                            ('transfer', 'Transfer'),
                            ('check', 'Bank Check'),
                        ],
                        max_length=20,
                        null=True,
                    ),
                ),
                (
                    'status',
                    models.CharField(
                        choices=[('open', 'Open'), ('finished', 'Finished')],
                        default='open',
                        max_length=20,
                    ),
                ),
                (
                    'client',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='application.client',
                    ),
                ),
                (
                    'product',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='application.product',
                    ),
                ),
                (
                    'silo',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='application.silo',
                    ),
                ),
            ],
            options={'abstract': False},
        ),
    ]