# Generated by Django 3.2.4 on 2021-06-13 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catolog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='cover',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='genre_set',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='storyline',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='summary',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
