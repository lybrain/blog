# Generated by Django 3.2.7 on 2021-10-06 08:59

import article.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(null=True, upload_to=article.models.article_directory_path),
        ),
    ]