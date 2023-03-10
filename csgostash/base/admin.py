from django.contrib import admin

# Register your models here.
from .models import Ak47, Weapon

admin.site.register(Ak47)

admin.site.register(Weapon)

