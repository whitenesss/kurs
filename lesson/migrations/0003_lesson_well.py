# Generated by Django 5.0.7 on 2024-07-10 22:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0002_initial'),
        ('well', '0002_remove_well_lesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='well',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='well.well', verbose_name='курс'),
        ),
    ]
