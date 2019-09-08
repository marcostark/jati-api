from django.db import models


class Event(models.Model):
    image = models.ImageField(upload_to = 'media/')
    title = models.CharField(max_length=255, verbose_name="Nome do Evento")
    type = models.CharField(max_length=255, verbose_name="Tipo do Evento")
    start_time = models.DateField(verbose_name="Data de Inicio")
    end_time = models.DateField(verbose_name="Data de termino")
    total_time = models.IntegerField(verbose_name="Carga Horaria")
    description = models.TextField(verbose_name="Descrição do evento")
    state = models.CharField(max_length=255, verbose_name="Estado")
    city = models.CharField(max_length=255, verbose_name="Cidade")
    street = models.CharField(verbose_name='Rua', max_length=500)
    street_number = models.CharField(max_length=8, verbose_name='Número')
    cep = models.CharField(verbose_name='CEP', max_length=9, blank=True, null=True)
    long = models.CharField(max_length=255, verbose_name="Longitude")
    lat = models.CharField(max_length=255, verbose_name="Latitude")
    instagram = models.CharField(max_length=255, verbose_name="Instagram")
    facebook = models.CharField(max_length=255, verbose_name="Facebook")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        verbose_name = 'Evento'
        verbose_name_plural = 'Evento'


