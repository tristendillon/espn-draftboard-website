from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
            
class Token(models.Model):
    TYPE_CHOICES = (
        ('frontend', 'Frontend'),
        ('extension', 'Chrome Extension'),
    )
    name = models.CharField(max_length=100)
    token_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    token = models.CharField(max_length=50)

@receiver(pre_save, sender=Token)
def generate_token(sender, instance, **kwargs):
    if not instance.token:
        instance.token = generate_token()