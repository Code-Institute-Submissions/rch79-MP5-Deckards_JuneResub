# Generated by Django 3.2 on 2022-05-10 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0004_book_sort_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='sort_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
