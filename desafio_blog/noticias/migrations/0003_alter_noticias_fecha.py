# Generated by Django 4.2.3 on 2023-07-21 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0002_alter_noticias_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='fecha',
            field=models.DateField(auto_now_add=True),
        ),
    ]
