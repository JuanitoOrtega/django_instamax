from django.db import models


class LandingPage(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Nombre')
    is_enabled = models.BooleanField(default=False, verbose_name='Habilitado')
    access_code = models.CharField(max_length=100, blank=True, null=True, verbose_name='Código de acceso')
    
    class Meta:
        verbose_name = 'LandingPage'
        verbose_name_plural = 'LandingPages'
        ordering = ['name']

    def __str__(self):
        return self.name