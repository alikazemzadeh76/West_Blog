# Generated by Django 4.1.7 on 2023-04-18 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='delivermassage',
            options={'verbose_name': 'پیام دریافتی', 'verbose_name_plural': 'پیام های دریافتی'},
        ),
        migrations.AlterModelOptions(
            name='editinformation',
            options={'verbose_name': 'راه ارتباط', 'verbose_name_plural': 'راه های ارتباطی'},
        ),
        migrations.AlterField(
            model_name='delivermassage',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='delivermassage',
            name='message',
            field=models.TextField(verbose_name='متن پیام'),
        ),
        migrations.AlterField(
            model_name='delivermassage',
            name='name',
            field=models.CharField(max_length=20, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='delivermassage',
            name='subject',
            field=models.CharField(max_length=50, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='editinformation',
            name='address',
            field=models.CharField(max_length=100, verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='editinformation',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='editinformation',
            name='phone_number',
            field=models.CharField(max_length=13, verbose_name='شماره تماس'),
        ),
    ]
