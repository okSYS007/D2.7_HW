# Generated by Django 4.0.4 on 2022-05-28 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='contentChoice',
            new_name='post_choice',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='content_rate',
            new_name='post_rate',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='content_text',
            new_name='post_text',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='content_title',
            new_name='post_title',
        ),
    ]
