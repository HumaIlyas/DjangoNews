# Generated by Django 3.2.18 on 2023-03-16 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0024_alter_category_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='post',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_category', to='news.post'),
        ),
    ]