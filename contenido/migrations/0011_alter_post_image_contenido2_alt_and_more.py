# Generated by Django 4.1.2 on 2022-12-21 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0010_alter_post_image_contenido2_paragraph_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_contenido2_alt',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_contenido2_paragraph',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_contenido2_title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_contenido3_alt',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_contenido3_paragraph',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_contenido3_title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_contenido4_alt',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_contenido4_paragraph',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_contenido4_title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_contenido_alt',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_contenido_paragraph',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_contenido_title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
