# Generated by Django 2.2 on 2019-08-25 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190825_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(verbose_name='Descrição do evento'),
        ),
    ]