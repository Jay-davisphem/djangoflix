# Generated by Django 3.2.13 on 2022-06-21 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_auto_20220621_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='publish_timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]