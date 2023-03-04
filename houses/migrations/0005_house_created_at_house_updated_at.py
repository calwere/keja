# Generated by Django 4.1.7 on 2023-03-04 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0004_house_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
