# Generated by Django 5.0.6 on 2024-05-29 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_blog_intro_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='intro_text',
            field=models.CharField(default='Stay curious, stay inspired, and let’s dive into the world of words together!'),
        ),
    ]
