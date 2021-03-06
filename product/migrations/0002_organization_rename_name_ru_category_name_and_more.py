# Generated by Django 4.0.3 on 2022-06-22 11:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='category',
            old_name='name_ru',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='definition_ru',
            new_name='info',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='name_ru',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='products',
            name='image',
        ),
        migrations.AddField(
            model_name='products',
            name='color',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('image', models.ImageField(default='products\\empty_cart.png', null=True, upload_to='products')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='product.products')),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='product.organization'),
        ),
    ]
