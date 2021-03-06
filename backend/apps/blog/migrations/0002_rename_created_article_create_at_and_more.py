# Generated by Django 4.0.4 on 2022-05-09 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='created',
            new_name='create_at',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='published',
            new_name='publish_at',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='updated',
            new_name='update_at',
        ),
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
