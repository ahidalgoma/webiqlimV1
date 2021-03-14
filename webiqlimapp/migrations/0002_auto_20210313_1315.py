# Generated by Django 3.1.7 on 2021-03-13 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webiqlimapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paramweb',
            old_name='efecto',
            new_name='efecto_imagen',
        ),
        migrations.AlterField(
            model_name='paramweb',
            name='idioma',
            field=models.CharField(choices=[('ES-EU', 'Español-Europa'), ('EN-EN', 'English-England')], help_text='Idioma de la web', max_length=5),
        ),
    ]
