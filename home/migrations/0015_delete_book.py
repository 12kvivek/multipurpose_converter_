# Generated by Django 3.2.5 on 2022-02-27 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_remove_book_book_no'),
    ]

    operations = [
        migrations.DeleteModel(
            name='book',
        ),
    ]
