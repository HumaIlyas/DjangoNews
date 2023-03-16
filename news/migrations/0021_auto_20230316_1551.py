# Generated by Django 3.2.18 on 2023-03-16 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0020_alter_category_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_tilte', to='news.post'),
        ),
        migrations.AlterField(
            model_name='category',
            name='post_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_post', to='news.post'),
        ),
    ]
