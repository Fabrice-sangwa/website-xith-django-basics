# Generated by Django 3.1.6 on 2023-04-07 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_blogpost_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=40)),
                ('wikipedia', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('price', models.FloatField(default=False, null=True)),
                ('summary', models.TextField(blank=True, null=True)),
                ('category', models.TextField(blank=True, default=['Aventure', 'Thriller', 'Fantastique', 'Romance', 'Horreur', 'Science-fiction'], null=True)),
                ('stock', models.IntegerField(default=0)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.author')),
            ],
        ),
    ]