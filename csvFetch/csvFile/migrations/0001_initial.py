# Generated by Django 5.0.1 on 2024-01-16 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Frame_Number', models.IntegerField()),
                ('Spot_Index', models.IntegerField()),
                ('Spot_Status', models.BooleanField()),
            ],
        ),
    ]
