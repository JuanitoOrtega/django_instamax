from django.db import models
import uuid


class Post(models.Model):
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False, verbose_name='ID')
    title = models.CharField(max_length=500, verbose_name='Titulo')
    artist = models.CharField(max_length=500, null=True, verbose_name='Artista')
    url = models.URLField(max_length=500, null=True, verbose_name='URL')
    image = models.URLField(max_length=500, verbose_name='Imagen')
    body = models.TextField(verbose_name='Contenido')
    tags = models.ManyToManyField('Tag', verbose_name='Etiquetas')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    
    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
        ordering = ['-created']

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=20, verbose_name='Nombre')
    slug = models.SlugField(max_length=20, unique=True, verbose_name='Slug')
    
    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'
    
    def __str__(self):
        return self.name