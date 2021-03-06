# Generated by Django 2.2.6 on 2020-10-19 10:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('posts', '0002_auto_20201003_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(unique=True,
                                   verbose_name='A part of yor Group URL'),
        ),
        migrations.AlterField(
            model_name='post',
            name='group',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.SET_NULL,
                                    parent_link=True, related_name='posts',
                                    to='posts.Group',
                                    verbose_name='Select a group to publish the post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(verbose_name='Make a good post today!'),
        ),
    ]
