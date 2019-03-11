from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # add additional fields in here
    bio = models.TextField(max_length=500,blank=True)
    dob = models.DateField(blank=True)
    country = models.CharField(max_length=500,blank=True)
    
    def __str__(self):
        return self.username