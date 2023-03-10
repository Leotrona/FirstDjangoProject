# Generated by Django 4.1.3 on 2023-03-10 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skin_name', models.CharField(max_length=50)),
                ('exterior', models.CharField(max_length=50)),
                ('nametag', models.CharField(blank=True, max_length=50, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
