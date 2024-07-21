from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.sites.models import Site
from django.core.mail import EmailMessage
from .models import InboxMessage


@receiver(post_save, sender=InboxMessage)
def send_email(sender, instance, created, **kwargs):
    message = instance
    site_domain = Site.objects.get(pk=1).domain
    # site_domain = Site.objects.get_current().domain
    
    if created:
        for participant in message.conversation.participants.all():
            if participant != message.sender and participant.emailaddress_set.filter(primary=True, verified=True).exists():
                try:
                    email_address = participant.emailaddress_set.get(primary=True, verified=True)
                    email_subject = f'Nuevo mensaje de {message.sender}'
                    email_body = f'Tengo buenas noticias para ti!\n\nHas recibido un nuevo mensaje en {site_domain}.'
                    email = EmailMessage(email_subject, email_body, to=[email_address.email])
                    email.send()
                except:
                    pass