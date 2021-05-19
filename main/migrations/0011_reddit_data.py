# Generated by Django 3.1.6 on 2021-04-04 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210402_0132'),
    ]

    operations = [
        migrations.CreateModel(
            name='reddit_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('display_name', models.CharField(max_length=200, null=True)),
                ('public_description', models.CharField(max_length=200, null=True)),
                ('verified', models.CharField(max_length=200, null=True)),
                ('is_gold', models.CharField(max_length=200, null=True)),
                ('total_karma', models.CharField(max_length=200, null=True)),
                ('created_utc', models.CharField(max_length=200, null=True)),
                ('icon_img', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]