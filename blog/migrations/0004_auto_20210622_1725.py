# Generated by Django 3.1.9 on 2021-06-22 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210622_1704'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='created_time',
            new_name='create_time',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='modified_time',
            new_name='modify_time',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='tui',
            new_name='recommend',
        ),
    ]