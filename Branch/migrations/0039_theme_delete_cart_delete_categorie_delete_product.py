# Generated by Django 4.2.5 on 2023-09-18 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Branch', '0038_alter_cart_price_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=5, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Categorie',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
