# Generated by Django 3.2.18 on 2023-03-16 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_alter_category_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='news.post'),
        ),
    ]
