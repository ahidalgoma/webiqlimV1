# Generated by Django 3.1.7 on 2021-03-13 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParamWeb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idioma', models.CharField(help_text='Idioma de la web', max_length=5)),
                ('mensaje_bienvenida', models.CharField(help_text='Mensaje de Bienvenida', max_length=50)),
                ('subtitulo_bienvenida', models.CharField(help_text='Subtítulo de Bienvenida', max_length=50)),
                ('titulo_menu', models.CharField(help_text='Título en el menú', max_length=50)),
                ('titulo_hoja', models.CharField(help_text='Título en la página', max_length=50)),
                ('contenido', models.TextField(blank=True, null=True)),
                ('imagen', models.ImageField(upload_to='weblimapp')),
                ('efecto', models.CharField(choices=[('A', 'Antes'), ('D', 'Después'), ('N', 'No aparece')], default='N', help_text='Lugar de aparición de la imagen', max_length=1)),
                ('activa', models.BooleanField(help_text='Si está activa esta será la que se publique')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'home',
            },
        ),
    ]
