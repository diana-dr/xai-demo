# Generated by Django 4.1.1 on 2022-11-24 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=100)),
                ('song', models.CharField(max_length=100)),
                ('duration_ms', models.IntegerField()),
                ('explicit', models.BooleanField()),
                ('year', models.IntegerField()),
                ('popularity', models.IntegerField()),
                ('danceability', models.FloatField()),
                ('energy', models.FloatField()),
                ('key', models.IntegerField()),
                ('loudness', models.FloatField()),
                ('mode', models.IntegerField()),
                ('speechiness', models.FloatField()),
                ('acousticness', models.FloatField()),
                ('instrumentalness', models.FloatField()),
                ('valence', models.FloatField()),
                ('liveness', models.FloatField()),
                ('tempo', models.FloatField()),
                ('genre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SongNormalize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=100)),
                ('song', models.CharField(max_length=100)),
                ('duration_ms', models.IntegerField()),
                ('explicit', models.BooleanField()),
                ('year', models.IntegerField()),
                ('popularity', models.IntegerField()),
                ('danceability', models.FloatField()),
                ('energy', models.FloatField()),
                ('key', models.IntegerField()),
                ('loudness', models.FloatField()),
                ('mode', models.IntegerField()),
                ('speechiness', models.FloatField()),
                ('acousticness', models.FloatField()),
                ('instrumentalness', models.FloatField()),
                ('valence', models.FloatField()),
                ('liveness', models.FloatField()),
                ('tempo', models.FloatField()),
                ('genre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TopSong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=100)),
                ('song', models.CharField(max_length=100)),
                ('duration_ms', models.IntegerField(null=True)),
                ('explicit', models.BooleanField(null=True)),
                ('year', models.IntegerField(null=True)),
                ('popularity', models.IntegerField(null=True)),
                ('danceability', models.FloatField(null=True)),
                ('energy', models.FloatField(null=True)),
                ('key', models.IntegerField(null=True)),
                ('loudness', models.FloatField(null=True)),
                ('mode', models.IntegerField(null=True)),
                ('speechiness', models.FloatField(null=True)),
                ('acousticness', models.FloatField(null=True)),
                ('instrumentalness', models.FloatField(null=True)),
                ('valence', models.FloatField(null=True)),
                ('liveness', models.FloatField(null=True)),
                ('tempo', models.FloatField(null=True)),
                ('genre', models.CharField(max_length=100)),
            ],
        ),
    ]
