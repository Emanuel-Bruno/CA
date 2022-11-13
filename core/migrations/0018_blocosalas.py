# Generated by Django 4.1.2 on 2022-11-13 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_remove_sala_bloco'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlocoSalas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Bloco de Sala',
                'verbose_name_plural': 'Blocos de Sala',
            },
        ),
    ]