# Generated by Django 3.1.5 on 2021-04-01 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_github_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='twitter_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('screem_name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('followers_count', models.CharField(max_length=200)),
                ('friend_count', models.CharField(max_length=200)),
                ('created_at', models.CharField(max_length=200)),
                ('verified', models.CharField(max_length=200)),
                ('last_tweet_time', models.CharField(max_length=200)),
                ('last_tweet', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
            ],
        ),
    ]
