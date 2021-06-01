from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    key = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', blank=True)
    title = models.TextField(max_length=20,blank=True)
    cover = models.ImageField(upload_to='images/')
    rate = models.IntegerField(default=0, editable=False)

    def __str__(self):
        return self.title
