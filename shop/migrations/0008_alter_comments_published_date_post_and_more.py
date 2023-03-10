# Generated by Django 4.1.7 on 2023-02-20 16:06

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0007_alter_comments_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 20, 16, 6, 33, 323835, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(default='', max_length=200, unique_for_date='published_date')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=20)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shop_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'News',
                'ordering': ('-published_date',),
            },
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='shop.post'),
        ),
        migrations.DeleteModel(
            name='News',
        ),
    ]
