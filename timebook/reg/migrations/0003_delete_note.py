# Generated by Django 5.1.3 on 2024-12-04 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0002_note'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Note',
        ),
    ]