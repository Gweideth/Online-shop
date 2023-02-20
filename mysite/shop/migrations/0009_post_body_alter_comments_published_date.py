# Generated by Django 4.1.7 on 2023-02-20 16:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_comments_published_date_post_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='comments',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 20, 16, 13, 14, 7924, tzinfo=datetime.timezone.utc)),
        ),
    ]
