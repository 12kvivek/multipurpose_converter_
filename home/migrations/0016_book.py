# Generated by Django 3.2.5 on 2022-02-27 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_delete_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('Sr_no', models.IntegerField(primary_key=True, serialize=False)),
                ('Book_name', models.CharField(max_length=60)),
                ('Publication', models.CharField(max_length=60)),
                ('Semester', models.IntegerField()),
                ('Edition', models.IntegerField()),
            ],
        ),
    ]
