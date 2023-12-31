# Generated by Django 4.2.4 on 2023-08-26 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('date_completed', models.DateField()),
                ('image', models.ImageField(upload_to='projects/images')),
            ],
        ),
    ]
