# Generated by Django 4.1.2 on 2022-11-13 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_sala'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sala',
            name='bloco',
        ),
    ]