# Generated by Django 3.2.18 on 2023-03-15 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20230315_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='post_category',
            field=models.CharField(max_length=100),
        ),
    ]