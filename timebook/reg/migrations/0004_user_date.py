# Generated by Django 5.1.3 on 2024-12-06 09:47

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0003_delete_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата'),
            preserve_default=False,
        ),
    ]