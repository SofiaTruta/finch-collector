# Generated by Django 4.2.7 on 2023-11-15 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_snack_alter_feeding_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='finch',
            name='snacks',
            field=models.ManyToManyField(to='main_app.snack'),
        ),
    ]
