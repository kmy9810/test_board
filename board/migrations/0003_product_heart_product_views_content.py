# Generated by Django 4.2 on 2023-04-08 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='heart',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='views_content',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
