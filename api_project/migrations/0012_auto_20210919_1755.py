# Generated by Django 3.2.7 on 2021-09-19 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_project', '0011_auto_20210919_1750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='temporaryurl',
            name='image',
        ),
        migrations.AddField(
            model_name='temporaryurl',
            name='image_id',
            field=models.IntegerField(default=None, verbose_name='Image ID'),
            preserve_default=False,
        ),
    ]
