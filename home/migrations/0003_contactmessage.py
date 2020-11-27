# Generated by Django 3.1.3 on 2020-11-18 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20201118_1505'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(blank=True, max_length=255)),
                ('subject', models.CharField(blank=True, max_length=255)),
                ('message', models.TextField(blank=True, max_length=255)),
                ('status', models.CharField(choices=[('Yangi', 'Yangi'), ("O'qildi", "O'qildi"), ('Yopilgan', 'Yopilgan')], default='Yangi', max_length=255)),
                ('ip', models.CharField(blank=True, max_length=255)),
                ('note', models.CharField(blank=True, max_length=255)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]