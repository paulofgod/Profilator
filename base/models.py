from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.urls import reverse
from datetime import datetime, date


# Create your models here.
class Login(AbstractUser):
    name = models.CharField(max_length=200, null= True)
    email = models.EmailField(unique=True, null=True)

    def __str__(self):
        return str(self.name)

class Bio(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to="images")
    description = models.TextField()
    author1 = models.CharField(max_length=255)
    author2 = models.CharField(max_length=255)
    author1_link_facebook = models.URLField(max_length=255)
    author2_link_linkedin = models.URLField(max_length=255)

    def __str__(self):
        return str(self.name)



    # def get_absolute_url(self):
    #     return reverse('home')
