# Generated by Django 2.2 on 2019-04-23 13:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_listing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='user introduction',
            new_name='audio_greeting',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='user offers',
            new_name='demand',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='trade completed',
            new_name='finished',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='user wants',
            new_name='supply',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='date posted',
        ),
        migrations.AddField(
            model_name='listing',
            name='post_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date posted'),
            preserve_default=False,
        ),
    ]