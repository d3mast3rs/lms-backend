# Generated by Django 3.2.9 on 2021-11-19 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_alter_book_users_who_issued'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='librarycard',
            name='num_of_books_issued',
        ),
    ]
