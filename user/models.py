from django.contrib.auth.models import User
from django.db import models

# Create your models here.



class Resume(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.CharField(blank=True, max_length=20)
    skills = models.CharField(blank=True, max_length=500)
    school = models.CharField(blank=True, max_length=200)
    grad_year = models.IntegerField(blank=True)


    def __str__(self):
        return self.user.username

    def user_name(self):
        return self.user.first_name + ' ' + self.user.last_name + ' [' + self.user.username + ']'

