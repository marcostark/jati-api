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


class Speaker(models.Model):
    first_name = models.CharField(max_length=255, verbose_name="Primeiro Nome")
    last_name = models.CharField(max_length=255, verbose_name="Último Nome")
    email = models.CharField(max_length=255, verbose_name="Email")
    speciality_institution = models.CharField(max_length=255, verbose_name="Cargo/Instituição")
    biography = models.CharField(max_length=255, verbose_name="Biografia")
    image = models.ImageField(upload_to = 'media/')
    lattes = models.CharField(max_length=255, verbose_name="Lattes")
    facebook = models.CharField(max_length=255, verbose_name="Facebook")
    linkedin = models.CharField(max_length=255, verbose_name="Linkedin")
    twitter = models.CharField(max_length=255, verbose_name="Twitter")
    github = models.CharField(max_length=255, verbose_name="Github")

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['-id']
        verbose_name = 'Convidado'
        verbose_name_plural = 'Convidados'


class Session(models.Model):
    title = models.CharField(max_length=255, verbose_name="Nome da Atividade")
    image = models.ImageField(upload_to = 'media/')
    type = models.CharField(max_length=255, verbose_name="Tipo da Atividade")
    start_time = models.DateTimeField(verbose_name="Hora de Inicio")
    total_time = models.CharField(max_length=255, verbose_name="Carga horaria")
    local = models.CharField(max_length=255, verbose_name="Local")
    description = models.CharField(max_length=255, verbose_name="Descrição")
    speaker = models.ForeignKey(Speaker, verbose_name="Convidado", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        verbose_name = 'Atividade'
        verbose_name_plural = 'Atividade'

