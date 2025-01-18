# Generated by Django 5.1.4 on 2025-01-16 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_category_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('image', models.ImageField(upload_to='offers/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
