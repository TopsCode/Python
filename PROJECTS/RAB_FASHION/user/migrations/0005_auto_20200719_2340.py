# Generated by Django 3.0.8 on 2020-07-19 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20200719_2241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Ordered', 'Ordered'), ('Shipped', 'Shipped'), ('Dispatched', 'Dispatched'), ('Delivered', 'Delivered')], max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.ColorVariation')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Product')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.SizeVariation')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Address'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Customer'),
        ),
    ]