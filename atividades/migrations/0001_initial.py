# Generated by Django 2.2 on 2019-09-08 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('convidados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Nome da Atividade')),
                ('image', models.ImageField(upload_to='media/')),
                ('type', models.CharField(max_length=255, verbose_name='Tipo da Atividade')),
                ('start_time', models.DateTimeField(verbose_name='Hora de Inicio')),
                ('total_time', models.CharField(max_length=255, verbose_name='Carga horaria')),
                ('local', models.CharField(max_length=255, verbose_name='Local')),
                ('description', models.CharField(max_length=255, verbose_name='Descrição')),
                ('speaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='convidados.Convidado', verbose_name='Convidado')),
            ],
            options={
                'verbose_name': 'Atividade',
                'verbose_name_plural': 'Atividade',
                'ordering': ['-id'],
            },
        ),
    ]
