# Generated by Django 4.1.2 on 2022-11-13 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_sala_bloco_salas'),
    ]

    operations = [
        migrations.AddField(
            model_name='turma',
            name='professor',
            field=models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.professor', verbose_name='Professor'),
        ),
        migrations.AddField(
            model_name='turma',
            name='sala',
            field=models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.sala', verbose_name='Sala'),
        ),
    ]