# Generated by Django 3.1.7 on 2021-03-14 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_publicar'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='efecto_imagen',
            field=models.CharField(choices=[('A', 'Antes'), ('D', 'Después'), ('I', 'Izquierda'), ('D', 'Derecha'), ('N', 'No aparece')], default='N', help_text='Lugar de aparición de la imagen al ver el post', max_length=1),
        ),
    ]
