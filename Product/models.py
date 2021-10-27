from django.db import models

# Create your models here.
class Commodity(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField(default='This is a description')
    is_new = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.name} of {self.price}'

    class Meta:
        verbose_name_plural="Commodity"
        ordering = ['-id']