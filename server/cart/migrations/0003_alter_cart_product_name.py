# Generated by Django 4.2.7 on 2023-11-17 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_alter_product_name"),
        ("cart", "0002_remove_cart_product_id_cart_product_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="product_name",
            field=models.ForeignKey(
                db_column="product_name",
                on_delete=django.db.models.deletion.CASCADE,
                to="product.product",
                to_field="name",
            ),
        ),
    ]
