# Generated by Django 4.2.4 on 2023-08-18 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_post_date_made'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.CharField(default='', max_length=100000000),
            preserve_default=False,
        ),
    ]