# Generated by Django 5.0.6 on 2024-06-02 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
        ('tasks', '0005_alter_task_author'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
    ]
