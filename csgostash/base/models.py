from django.db import models
from django.contrib.auth.models import User
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
    

WEAPON_TYPES = (
    ('rifle', 'RIFLE'),
    ('knife', 'KNIFE'),
    ('heavy', 'HEAVY'),
    ('pistol', 'PISTOL'),
    ('smg','SMG'),
)



class Weapon(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    weapon_type = models.CharField(max_length=6, choices=WEAPON_TYPES, default='green')
    skin_name = models.CharField(max_length=50)
    skin_float = models.FloatField(default=0.00)
    price = models.FloatField(default=0.00)
    is_stattrak = models.BooleanField(default=False)
    exterior = models.CharField(max_length=50)
    nametag = models.CharField(max_length=50, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering = ['price', 'skin_name']

    def __str__(self):
        return self.skin_name