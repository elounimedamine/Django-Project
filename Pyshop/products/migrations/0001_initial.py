# Generated by Django 4.0.4 on 2022-05-03 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('image_url', models.ImageField(blank=True, upload_to='images')),
            ],
        ),
    ]
