# Generated by Django 3.1.7 on 2021-04-01 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210401_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='github_data',
            name='bio',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='github_data',
            name='created_at',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='github_data',
            name='followers',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='github_data',
            name='following',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='github_data',
            name='link',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='github_data',
            name='location',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='github_data',
            name='login',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='github_data',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='github_data',
            name='public_repos',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='github_data',
            name='updated_at',
            field=models.CharField(max_length=200, null=True),
        ),
    ]