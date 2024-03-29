# Generated by Django 4.2.1 on 2023-05-27 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_color_title_alter_generalcategory_title_and_more'),
        ('customer', '0006_alter_wishitem_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasketItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.color')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basket', to='customer.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.products')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.size')),
            ],
        ),
    ]
