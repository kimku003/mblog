# Generated by Django 5.0.3 on 2024-04-13 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mblog', '0008_profileimage_delete_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
