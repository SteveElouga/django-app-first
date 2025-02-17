from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    class Role(models.TextChoices):
        CREATOR='Creator'
        SUBSCRIBER='Subscriber'
        
    profile_photo = models.ImageField(verbose_name='Photo de profile')
    role = models.CharField(max_length=50, verbose_name='role', choices=Role.choices, default=Role.SUBSCRIBER)
