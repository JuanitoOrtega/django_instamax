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


class Comment(models.Model):
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key = True, editable=False, verbose_name='ID')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comments', verbose_name='Autor')
    parent_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='Publicación')
    body = models.CharField(max_length=150, verbose_name='Comentario')
    likes = models.ManyToManyField(User, related_name='likedcomments', through='LikedComment', verbose_name='Me gusta')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ['-created']
        
    def __str__(self):
        try:
            return f'{self.author.username} : {self.body[:30]}' 
        except:
            return f'no author : {self.body[:30]}'
        
        
class LikedComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, verbose_name='Comentario')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    
    class Meta:
        verbose_name = 'Comentario | Me gusta'
        verbose_name_plural = 'Comentario | Me gusta'
    
    def __str__(self):
        return f'{self.user.username} : {self.comment.body[:30]}'
        
        
class Reply(models.Model):
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key = True, editable=False, verbose_name='ID')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="replies", verbose_name='Autor')
    parent_comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="replies", verbose_name='Comentario')
    body = models.CharField(max_length=150, verbose_name='Respuesta')
    likes = models.ManyToManyField(User, related_name='likedreplies', through='LikedReply', verbose_name='Me gusta')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

    class Meta:
        verbose_name = 'Respuesta'
        verbose_name_plural = 'Respuestas'
        ordering = ['created']
        
    def __str__(self):
        try:
            return f'{self.author.username} : {self.body[:30]}'
        except:
            return f'no author : {self.body[:30]}'
        
        
class LikedReply(models.Model):
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE, verbose_name='Respuesta')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    
    class Meta:
        verbose_name = 'Respuesta | Me gusta'
        verbose_name_plural = 'Respuesta | Me gusta'
    
    def __str__(self):
        return f'{self.user.username} : {self.reply.body[:30]}'