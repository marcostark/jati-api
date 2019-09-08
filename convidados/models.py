from django.db import models

class Convidado(models.Model):
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
