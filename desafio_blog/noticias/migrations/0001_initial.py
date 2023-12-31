# Generated by Django 4.2.3 on 2023-07-20 23:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('titulo', models.CharField(max_length=100)),
                ('texto', models.TextField()),
                ('autor_noticia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autor_noticias', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
