# Generated by Django 5.0.8 on 2024-12-13 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_link_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Small',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('foto', models.ImageField(upload_to='')),
            ],
        ),
    ]
