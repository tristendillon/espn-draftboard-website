from django.db import models
from .utils.token_utils import generate_token

class Token(models.Model):
    TYPE_CHOICES = (
        ('frontend', 'Frontend'),
        ('extension', 'Chrome Extension'),
    )
    token_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    token = models.CharField(max_length=255, default=generate_token)

    @classmethod
    def set_new_token(cls, token_type, new_token):
        existing_token = cls.objects.filter(token_type=token_type).first()
        if existing_token:
            existing_token.delete()

        return cls.objects.create(token_type=token_type, token=new_token)
