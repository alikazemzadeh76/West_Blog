# Generated by Django 4.1.7 on 2023-03-31 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_app', '0006_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
