# Generated by Django 4.1.7 on 2023-03-24 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='image/article_app'),
        ),
    ]
