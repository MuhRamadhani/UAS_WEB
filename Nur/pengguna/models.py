from django.db import models
from django.contrib.auth.models import User

class Biodata(models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE)
    alamat = models.TextField(blank=True, null=True)
    telpon = models.CharField(max_length=20, blank=True, null=True)
    foto = models.ImageField(upload_to='pengguna', blank=True, null=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural = "1. Biodata"

# Create your models here.
