# Generated by Django 4.1.2 on 2022-11-03 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_curso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField(null=True, verbose_name='Data Inicial')),
                ('data_final', models.DateField(null=True, verbose_name='Data Final')),
            ],
            options={
                'verbose_name': 'Período',
                'verbose_name_plural': 'Períodos',
            },
        ),
    ]
