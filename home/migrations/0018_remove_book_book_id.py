# Generated by Django 3.2.5 on 2022-02-27 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_book_book_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='Book_id',
        ),
    ]
