# Generated by Django 3.1.2 on 2020-11-11 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsBlog', '0002_auto_20201021_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.CharField(blank=True, default='WLUHO9A_xik', max_length=50),
        ),
    ]
