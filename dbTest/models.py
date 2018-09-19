from django.db import models

# Create your models here.

class User(models.Model):
    gender=(
        ('male','M'),
        ('female','F')
    )
    username = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32,choices=gender, default='M')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['c_time']
        verbose_name = 'user'
        verbose_name_plural = 'user'


