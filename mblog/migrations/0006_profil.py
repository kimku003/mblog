# Generated by Django 5.0.3 on 2024-04-12 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mblog', '0005_delete_userinfo_post_image_post_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/img')),
                ('video', models.FileField(blank=True, null=True, upload_to='media/videos')),
            ],
        ),
    ]
