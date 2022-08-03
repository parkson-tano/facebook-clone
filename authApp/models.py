import email
from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length= 100)
    mobile_number = models.CharField(max_length=255)
    birthday = models.DateField()
    gender = models.CharField(max_length=10)
    pronoun = models.CharField(max_length=20, blank=True, null=True)
    optional_gender = models.CharField(max_length=25, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
    