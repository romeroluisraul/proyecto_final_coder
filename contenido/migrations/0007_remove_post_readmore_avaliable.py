# Generated by Django 4.1.2 on 2022-12-14 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0006_alter_post_text_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='readmore_avaliable',
        ),
    ]