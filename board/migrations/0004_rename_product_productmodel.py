# Generated by Django 4.2 on 2023-04-09 03:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0003_product_heart_product_views_content'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='ProductModel',
        ),
    ]