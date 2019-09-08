from django.db import models
from convidados.models import Convidado

class Atividade(models.Model):
    title = models.CharField(max_length=255, verbose_name="Nome da Atividade")
    image = models.ImageField(upload_to = 'media/')
    type = models.CharField(max_length=255, verbose_name="Tipo da Atividade")
    start_time = models.DateTimeField(verbose_name="Hora de Inicio")
    total_time = models.CharField(max_length=255, verbose_name="Carga horaria")
    local = models.CharField(max_length=255, verbose_name="Local")
    description = models.CharField(max_length=255, verbose_name="Descrição")
    speaker = models.ForeignKey(Convidado, verbose_name="Convidado", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        verbose_name = 'Atividade'
        verbose_name_plural = 'Atividade'
