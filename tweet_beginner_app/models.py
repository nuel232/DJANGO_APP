from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    text = models.TextField(max_length = 300)
    photo = models.ImageField(upload_to='photos/', blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    temperature = models.FloatField(null=True, blank=True)
    weather_description = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.text[:10]}'
    
