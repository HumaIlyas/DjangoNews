# Generated by Django 3.2.18 on 2023-03-30 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0030_alter_post_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='comment',
        ),
    ]
