# Generated by Django 3.2.5 on 2022-03-01 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_book_edition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Edition',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
