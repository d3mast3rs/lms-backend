# Generated by Django 3.2.9 on 2021-11-19 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_rename_user_id_librarycard_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='librarycard',
            old_name='id',
            new_name='user_id',
        ),
    ]