# Generated by Django 4.2.7 on 2023-12-02 10:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('vender', '0003_alter_purchaseorder_po_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='delivery_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='issue_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='items',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='order_completed_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='po_number',
            field=models.CharField(default=uuid.UUID('fa08a14f-42a4-4d2d-83e1-a6a53f570eb5'), max_length=50),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('completed', 'completed'), ('canceled', 'canceled')], default='pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='venderprofile',
            name='vender_code',
            field=models.CharField(default='1E49F0', max_length=30),
        ),
    ]