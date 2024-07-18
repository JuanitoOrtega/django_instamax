from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.timesince import timesince
from cryptography.fernet import Fernet
from django.conf import settings
import uuid


class InboxMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages", verbose_name="Remitente")
    conversation = models.ForeignKey('Conversation', on_delete=models.CASCADE, related_name="messages", verbose_name="Conversación")
    body = models.TextField(verbose_name="Mensaje")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    
    class Meta:
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes"
        ordering = ['-created']
        
    def __str__(self):
        time_since = timesince(self.created, timezone.now())
        return f'[{self.sender.username} : {time_since} ago]'
    
    
class Conversation(models.Model):
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False, verbose_name="ID")
    participants = models.ManyToManyField(User, related_name='conversations', verbose_name="Participantes")
    lastmessage_created = models.DateTimeField(default=timezone.now, verbose_name="Último mensaje")
    is_seen = models.BooleanField(default=False, verbose_name="Visto")
    
    class Meta:
        verbose_name = "Conversación"
        verbose_name_plural = "Conversaciones"
        ordering = ['-lastmessage_created']
        
    def __str__(self):
        user_names = ", ".join(user.username for user in self.participants.all())
        return f'[{user_names}]'