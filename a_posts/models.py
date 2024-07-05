from django.db import models
from django.contrib.auth.models import User
import uuid


class Post(models.Model):
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False, verbose_name='ID')
    title = models.CharField(max_length=500, verbose_name='Titulo')
    artist = models.CharField(max_length=500, null=True, verbose_name='Artista')
    url = models.URLField(max_length=500, null=True, verbose_name='URL')
    image = models.URLField(max_length=500, verbose_name='Imagen')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='posts', verbose_name='Autor')
    body = models.TextField(verbose_name='Contenido')
    likes = models.ManyToManyField(User, related_name="likedposts", through="LikedPost", verbose_name='Me gusta')
    tags = models.ManyToManyField('Tag', verbose_name='Etiquetas')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    
    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
        ordering = ['-created']
    
    def get_absolute_url(self):
        return f'/post/{self.id}'

    def __str__(self):
        return self.title


class LikedPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Publicación')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    
    class Meta:
        verbose_name = 'Me gusta'
        verbose_name_plural = 'Me gusta'
    
    def __str__(self):
        return f'{self.user.username} : {self.post.title}'


class Tag(models.Model):
    name = models.CharField(max_length=20, verbose_name='Nombre')
    image = models.FileField(upload_to='icons/', null=True, blank=True, verbose_name='Icono')
    slug = models.SlugField(max_length=20, unique=True, verbose_name='Slug')
    order = models.IntegerField(null=True, verbose_name='Orden')
    
    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'    
        ordering = ['order']

    def get_absolute_url(self):
        return f'/category/{self.slug}/'
    
    def __str__(self):
        return self.name