from django.db import models


class Feature(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Nombre')
    developer = models.CharField(max_length=255, unique=True, verbose_name='Desarrollador')
    staging_enabled = models.BooleanField(default=False, verbose_name='Habilitado en Staging')
    production_enabled = models.BooleanField(default=False, verbose_name='Habilitado en Producción')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    
    class Meta:
        verbose_name = 'Característica'
        verbose_name_plural = 'Características'
        ordering = ['-created']

    def __str__(self):
        return self.name