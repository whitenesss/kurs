# Generated by Django 5.0.7 on 2024-07-10 22:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lesson', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Well',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='название')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog', verbose_name='изображение')),
                ('content', models.TextField(verbose_name='содержание')),
                ('lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lesson.lesson', verbose_name='урок')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='well_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'выпускной блок',
                'verbose_name_plural': 'выпускные блоки',
            },
        ),
    ]