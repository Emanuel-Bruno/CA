# Generated by Django 4.1.2 on 2022-11-13 19:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0027_tarefaturma'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefaturma',
            name='data_atualizacao',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Data de Atualização'),
        ),
        migrations.AddField(
            model_name='tarefaturma',
            name='data_criacao',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data de Criação'),
        ),
        migrations.AddField(
            model_name='tarefaturma',
            name='usuario_criacao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_requests_created', to=settings.AUTH_USER_MODEL, verbose_name='Usuário de Criação'),
        ),
    ]