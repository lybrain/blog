# Generated by Django 3.2.7 on 2021-10-27 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_alter_article_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='views',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]