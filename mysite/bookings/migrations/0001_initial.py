# Generated by Django 3.1.2 on 2020-10-22 22:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('artist_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('rider', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party', models.CharField(max_length=200)),
                ('date', models.DateTimeField(verbose_name='day of the party')),
                ('fee', models.IntegerField(default=0)),
                ('hosting', models.IntegerField(default=0)),
            ],
        ),
    ]