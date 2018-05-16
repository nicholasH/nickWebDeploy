# Generated by Django 2.0.5 on 2018-05-16 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='businessCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('contact_name', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
