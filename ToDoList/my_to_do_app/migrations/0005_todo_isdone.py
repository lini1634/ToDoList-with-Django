# Generated by Django 2.2.1 on 2020-08-22 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_to_do_app', '0004_remove_todo_isdone'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='isDone',
            field=models.BooleanField(default=False),
        ),
    ]