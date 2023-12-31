# Generated by Django 4.1.7 on 2023-03-29 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='test_field',
            field=models.BinaryField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile/image'),
        ),
    ]
