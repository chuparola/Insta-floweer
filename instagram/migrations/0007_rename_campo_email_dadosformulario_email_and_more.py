# Generated by Django 4.2.7 on 2023-12-06 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0006_remove_dadosformulario_campo1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dadosformulario',
            old_name='campo_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='dadosformulario',
            old_name='campo_usuario',
            new_name='usuario',
        ),
    ]
