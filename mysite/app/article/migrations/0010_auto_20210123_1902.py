# Generated by Django 3.1 on 2021-01-23 19:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0009_presents'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Presents',
            new_name='Present',
        ),
    ]