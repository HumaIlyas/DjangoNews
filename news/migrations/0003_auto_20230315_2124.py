# Generated by Django 3.2.18 on 2023-03-15 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='news',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='news_category',
            new_name='post_category',
        ),
    ]