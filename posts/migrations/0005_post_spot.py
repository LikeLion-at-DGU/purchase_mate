# Generated by Django 3.1.6 on 2021-08-09 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='spot',
            field=models.CharField(max_length=200, null=True),
        ),
    ]