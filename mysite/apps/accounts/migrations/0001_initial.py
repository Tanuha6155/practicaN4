# Generated by Django 3.2.2 on 2021-06-18 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_in', models.DateTimeField(auto_now_add=True)),
                ('time_out', models.DateTimeField(null=True)),
                ('cost', models.FloatField(default=0.0)),
                ('take_away', models.BooleanField(default=False)),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField(default=0.0)),
                ('composition', models.TextField(default='Состав не указан')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('labor_contract', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='accounts.ProductOrder', to='accounts.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.staff'),
        ),
    ]