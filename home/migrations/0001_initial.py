# Generated by Django 3.1.3 on 2020-11-13 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('keywords', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('about', models.TextField()),
                ('contact', models.TextField()),
                ('facebook', models.CharField(blank=True, max_length=255)),
                ('instagram', models.CharField(blank=True, max_length=255)),
                ('telegram', models.CharField(blank=True, max_length=255)),
                ('youtube', models.CharField(blank=True, max_length=255)),
                ('tiktok', models.CharField(blank=True, max_length=255)),
                ('gmail', models.EmailField(blank=True, max_length=255)),
                ('email', models.EmailField(blank=True, max_length=255)),
                ('twitter', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
