# Generated by Django 4.2.1 on 2023-05-27 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0009_alter_basketitem_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=20)),
                ('discount', models.FloatField()),
                ('expire', models.DateTimeField()),
                ('limit', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('used_customers', models.ManyToManyField(blank=True, related_name='used_coupons', to='customer.customer')),
            ],
        ),
    ]
