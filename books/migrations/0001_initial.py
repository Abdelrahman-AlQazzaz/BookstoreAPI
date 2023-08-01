# Generated by Django 4.2.3 on 2023-08-01 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=20)),
                ('publication_date', models.DateField()),
                ('price', models.FloatField()),
            ],
        ),
    ]
