# Generated by Django 3.2.18 on 2023-04-04 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_post_unlikes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='unlikes',
        ),
    ]