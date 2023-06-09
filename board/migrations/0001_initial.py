# Generated by Django 4.2 on 2023-04-09 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('자유게시판', '자유게시판'), ('익명게시판', '익명게시판')], max_length=5)),
                ('title', models.CharField(max_length=20)),
                ('content', models.CharField(default='', max_length=256)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('heart', models.IntegerField()),
                ('views_content', models.IntegerField()),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]
