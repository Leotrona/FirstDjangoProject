from django.db import models

# Create your models here.

class Ak47(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    id = models.IntegerField
    float = models.FloatField
    statrak = models.CharField(max_length=20)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    