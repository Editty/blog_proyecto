# Generated by Django 4.2.3 on 2023-07-16 01:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('publicaciones', '0004_publicaciones_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicaciones',
            name='creador_del_posteo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='posteos_usuario', to=settings.AUTH_USER_MODEL),
        ),
    ]