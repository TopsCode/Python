# Generated by Django 2.2.5 on 2020-05-12 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0037_auto_20200511_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='s_city',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='shop',
            name='s_contact',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
