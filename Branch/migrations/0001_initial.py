# Generated by Django 4.0 on 2022-08-25 07:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('sitle', models.CharField(max_length=20, null=True, unique=True)),
                ('slug', models.SlugField(max_length=20, unique=True)),
                ('author', models.CharField(max_length=20, null=True)),
                ('preamble', models.CharField(max_length=68, null=True)),
                ('description', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='Images')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('d', 'Draft'), ('p', 'Publish')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20, null=True)),
                ('sitle', models.CharField(max_length=20, null=True, unique=True)),
                ('slug', models.SlugField(max_length=20, unique=True)),
                ('teacher', models.CharField(max_length=20, null=True)),
                ('topic', models.CharField(max_length=20, null=True)),
                ('preamble', models.CharField(max_length=90, null=True)),
                ('thumbnail', models.ImageField(upload_to='Images')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('d', 'Draft'), ('p', 'Publish')], max_length=1)),
            ],
        ),
    ]
