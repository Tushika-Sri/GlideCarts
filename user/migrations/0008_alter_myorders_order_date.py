# Generated by Django 4.2.4 on 2023-09-20 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_rename_added_date_myorders_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myorders',
            name='order_date',
            field=models.DateField(null=True),
        ),
    ]
