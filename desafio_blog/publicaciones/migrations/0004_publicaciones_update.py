# Generated by Django 4.2.3 on 2023-07-13 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0003_alter_categoria_actualizacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicaciones',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]