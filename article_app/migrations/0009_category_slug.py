# Generated by Django 4.1.7 on 2023-04-03 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_app', '0008_alter_article_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
