# Generated by Django 4.1.3 on 2023-01-01 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=30)),
                ('translate_short', models.CharField(max_length=10)),
                ('recognition_short', models.CharField(max_length=10)),
            ],
        ),
    ]
