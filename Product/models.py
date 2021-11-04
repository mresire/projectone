from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Commodity(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField(default='This is a description')
    is_new = models.BooleanField(default=False)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    img = models.FileField(blank=True,null=True,upload_to="images/")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural="Commodity"
        ordering = ['-id']

class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title}'

class Song(models.Model):
    title = models.CharField(max_length=100)
    album = models.ForeignKey(to=Album,on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.title} from {self.album}'


class Author(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=400)

    def __str__(self):
        return f'{self.name}'

    
class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    authors = models.ManyToManyField(Author)
    
    def __str__(self):
        return f'{self.title}'