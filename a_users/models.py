from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuario')
    image = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name='Imagen')
    realname = models.CharField(max_length=100, null=True, blank=True, verbose_name='Nombre real')
    email = models.EmailField(unique=True, null=True, verbose_name='Correo electrónico')
    location = models.CharField(max_length=50, null=True, blank=True, verbose_name='Ubicación')
    bio = models.TextField(null=True, blank=True, verbose_name='Biografía')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        
    @property
    def avatar(self):
        try:
            avatar = self.image.url
        except:
            avatar = static('images/avatar_default.svg')
        return avatar
    
    @property
    def name(self):
        if self.realname:
            name = self.realname
        else:
            name = self.user.username 
        return name
    
    def __str__(self):
        return self.user.username