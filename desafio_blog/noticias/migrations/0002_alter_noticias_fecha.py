# Generated by Django 4.2.3 on 2023-07-20 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='fecha',
            field=models.DateField(),
        ),
    ]
