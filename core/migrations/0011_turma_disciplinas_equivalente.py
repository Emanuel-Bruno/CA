# Generated by Django 4.1.2 on 2022-11-03 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_disciplina'),
    ]

    operations = [
        migrations.AddField(
            model_name='turma',
            name='disciplinas_equivalente',
            field=models.ManyToManyField(null=True, to='core.disciplina', verbose_name='Disciplina'),
        ),
    ]
