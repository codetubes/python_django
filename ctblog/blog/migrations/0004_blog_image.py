# Generated by Django 3.0.2 on 2020-04-05 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='blog_posts/'),
        ),
    ]
