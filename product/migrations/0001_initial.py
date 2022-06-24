# Generated by Django 4.0.3 on 2022-06-22 10:53

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name_ru', models.CharField(max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(default='products\\empty_cart.png', null=True, upload_to='category')),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('value', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('definition_ru', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(default='products\\empty_cart.png', null=True, upload_to='products')),
                ('price', models.FloatField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('material', models.CharField(blank=True, max_length=100, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='product.category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('total', models.IntegerField(default=1)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('burger', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.products')),
            ],
        ),
    ]