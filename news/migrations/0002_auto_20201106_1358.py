# Generated by Django 3.1 on 2020-11-06 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='featured',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='video',
            name='slider',
            field=models.BooleanField(default=False),
        ),
    ]
