# Generated by Django 4.1.5 on 2023-01-25 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='productMainModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('uniquecode', models.BooleanField(default=True)),
                ('size', models.CharField(blank=True, choices=[('10', '10'), ('20', '20'), ('30', '30')], max_length=5)),
                ('quality', models.CharField(blank=True, choices=[('high', 'High'), ('low', 'Low'), ('medium', 'Medium')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='productImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productmainmodel')),
            ],
        ),
        migrations.CreateModel(
            name='productColourModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colour', models.CharField(blank=True, choices=[('red', 'Red'), ('blue', 'Blue'), ('green', 'Green'), ('black', 'Black')], max_length=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productmainmodel')),
            ],
        ),
    ]