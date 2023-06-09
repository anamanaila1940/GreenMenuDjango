# Generated by Django 4.1.7 on 2023-05-04 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0016_remove_product_mistake_remove_product_quantity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='mistake',
            field=models.CharField(choices=[('Mistake', 'Mistake'), ('No mistake', 'No mistake')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.FloatField(null=True),
        ),
        migrations.DeleteModel(
            name='Mistake',
        ),
    ]
