from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import producer

class Users(models.Model):
    username = models.CharField(max_length=100)

@receiver(post_save, sender=Users)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        mensagem = instance.username
        producer.delay(mensagem)