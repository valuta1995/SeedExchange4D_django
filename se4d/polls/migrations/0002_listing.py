# Generated by Django 2.2 on 2019-04-23 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date posted', models.DateTimeField()),
                ('user offers', models.CharField(max_length=63)),
                ('user wants', models.CharField(max_length=63)),
                ('user introduction', models.URLField()),
                ('trade completed', models.BooleanField()),
            ],
        ),
    ]
