# Generated by Django 3.2.9 on 2021-11-19 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_auto_20211119_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='users_who_issued',
            field=models.ManyToManyField(blank=True, related_name='books_issued', to='library.LibraryCard'),
        ),
    ]