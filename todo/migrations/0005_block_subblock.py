# Generated by Django 3.1 on 2020-02-08 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_subtask'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('begin_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.User')),
            ],
        ),
        migrations.CreateModel(
            name='SubBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.Block')),
            ],
        ),
    ]
