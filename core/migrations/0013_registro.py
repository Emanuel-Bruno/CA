# Generated by Django 4.1.2 on 2022-11-03 03:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_turma_disciplinas_equivalente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota1', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Nota 1ª Unidade')),
                ('nota2', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Nota 2ª Unidade')),
                ('nota3', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Nota 3ª Unidade')),
                ('nota_recuperacao', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Nota da Recuperacao')),
                ('aluno', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.aluno', verbose_name='Aluno')),
                ('turma', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.turma', verbose_name='Turma')),
            ],
            options={
                'verbose_name': 'Registro',
                'verbose_name_plural': 'Registros',
            },
        ),
    ]
