# Generated by Django 4.1.2 on 2022-12-14 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0005_commentary_related_post_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text_content',
            field=models.TextField(blank=True, max_length=7000),
        ),
    ]
