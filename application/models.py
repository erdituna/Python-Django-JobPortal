from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import ModelForm

from job.models import Job


class Application(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Canceled', 'Canceled'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    salary = models.IntegerField()
    title = models.CharField(max_length=150)
    company = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    adminnote = models.CharField(blank=True, max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.job.title

class AppForm(ModelForm):
    class Meta:
        model = Application
        fields = ['first_name','last_name','salary','title','company']

