# Generated by Django 4.1.7 on 2023-04-18 08:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article_app', '0014_rename_create_time_article_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='article_app.comment', verbose_name='پاسخ به'),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', to='article_app.article', verbose_name='مقاله')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'لایک',
                'verbose_name_plural': 'لایک ها',
            },
        ),
    ]
