# Generated by Django 4.2.5 on 2023-09-22 03:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('customer', models.CharField(max_length=255, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer_identification', models.CharField(max_length=25, null=True)),
                ('card_number', models.CharField(max_length=25, null=True)),
            ],
            options={
                'verbose_name': 'Pagamento',
                'verbose_name_plural': 'Pagamentos',
                'db_table': 'payment',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('fiscal_identification', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('phone', models.CharField(max_length=25, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('address', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentStatus',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(choices=[('COMPLETED', 'COMPLETED'), ('CANCELED', 'CANCELED')], default='COMPLETED', max_length=10)),
                ('description', models.CharField(max_length=255, null=True)),
                ('meta_data', models.JSONField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_status', to='payment.payment')),
            ],
            options={
                'verbose_name': 'Status do pagamento',
                'verbose_name_plural': 'Status dos pagamentos',
                'db_table': 'payment_status',
                'ordering': ['created_at'],
            },
        ),
        migrations.AddField(
            model_name='payment',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='payment.store'),
        ),
    ]
