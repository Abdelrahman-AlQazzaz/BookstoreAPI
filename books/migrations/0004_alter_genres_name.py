# Generated by Django 4.2.3 on 2023-08-04 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_authors_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genres',
            name='name',
            field=models.SlugField(max_length=100),
        ),
    ]
