# Generated by Django 3.2.5 on 2022-03-01 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_remove_book_book_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='Edition',
        ),
    ]
