# Generated by Django 3.1 on 2020-02-08 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_block_subblock'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='on_days',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]