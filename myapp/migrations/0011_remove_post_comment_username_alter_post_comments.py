# Generated by Django 4.2.4 on 2023-08-19 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_post_comment_username_post_post_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comment_username',
        ),
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.CharField(max_length=1000000000),
        ),
    ]
