# Generated by Django 4.2.1 on 2023-05-29 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_pay'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pay',
            options={'verbose_name': 'Оплата', 'verbose_name_plural': 'Оплата товару'},
        ),
        migrations.AddField(
            model_name='pay',
            name='cat',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.PROTECT, to='shop.category', verbose_name='Категорії'),
        ),
        migrations.AddField(
            model_name='pay',
            name='content',
            field=models.TextField(blank=True, verbose_name='Опис товару'),
        ),
        migrations.AddField(
            model_name='pay',
            name='price',
            field=models.CharField(default=True, max_length=20, verbose_name='Ціна'),
        ),
    ]
