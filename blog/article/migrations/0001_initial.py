# Generated by Django 4.0.4 on 2022-05-26 11:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Public'), (2, 'Private')], default=0)),
                ('desc', models.CharField(max_length=200)),
                ('content', models.TextField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddIndex(
            model_name='article',
            index=models.Index(fields=['title'], name='article_art_title_d15895_idx'),
        ),
        migrations.AddIndex(
            model_name='article',
            index=models.Index(fields=['author'], name='article_art_author__71ab43_idx'),
        ),
    ]
