from django.db import models

# Create your models here.
# Clases enlazadas a la bbdd
# Esto es una tabla dentro de la bbdd
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    link = models.URLField(null=True, blank=True) # link
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación") # fecha de creación
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición") # fecha de edición
    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        #campo de ordenacion, del más nuevo al más antiguo
        ordering = ['-created']


    def __str__(self):
        return self.title