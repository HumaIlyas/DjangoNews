# Generated by Django 3.2.18 on 2023-03-16 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
    ]