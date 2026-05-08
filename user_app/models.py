import random
import string

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(
        max_length= 150,
        blank= True,
        null= True
    )

    email = models.EmailField(
        unique= True
    )

    is_active = False

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Profile(models.Model):
    """
    
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blank = models.DateField(null=True, blank=True)
    signature = models.ImageField(blank=True, null=True)
    avatar = models.ImageField()
    pseudonym = models.CharField(max_length= 50)
    is_image_signature = models.BooleanField()
    is_text_signature = models.BooleanField()

class Album(models.Model):
    """
    
    """
    name = models.CharField(max_length=100)
    theme = models.CharField(max_length= 50)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_created=True)
    is_shown = models.BooleanField()
