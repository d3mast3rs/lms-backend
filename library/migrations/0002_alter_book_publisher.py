# Generated by Django 3.2.9 on 2021-11-19 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='books', to='library.publisher'),
        ),
    ]
