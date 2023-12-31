# Generated by Django 4.2.3 on 2023-07-13 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, unique=True)),
                ('activo', models.BooleanField(default=True)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('actualizacion', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.AddField(
            model_name='publicaciones',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posteos', to='publicaciones.categoria'),
        ),
    ]
