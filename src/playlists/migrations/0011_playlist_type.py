# Generated by Django 3.2.13 on 2022-06-24 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0010_seasonproxy_tvshowproxy_tvshowseasonproxy'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='type',
            field=models.CharField(choices=[('MOV', 'Movie'), ('TVS', 'TV Show'), ('SEA', 'Season'), ('PLY', 'Playlist')], default='PLY', max_length=3),
        ),
    ]
