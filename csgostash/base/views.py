from django.shortcuts import render
from .models import Weapon
from django.http import HttpResponseNotFound

# Create your views here.


def home(request):
    return render(request, 'home.html')

def rifles(request):
    return render(request, 'rifles.html')

def knives(request):
    return render(request, 'knives.html')

def pistols(request):
    return render(request, 'pistols.html')

def smg(request):
    return render(request,'smg.html')

def cases(request):
    return render(request, 'cases.html')

def stickers(request):
    return render(request,'stickers.html')

def heavy(request):
    return render(request, 'heavy.html')

def gloves(request):
    return render(request, 'gloves.html')

def existing_skins(request, weapon):
    
        if weapon == 'a':
            return HttpResponseNotFound("Item not found!")
        
        weapons = Weapon.objects.filter(skin_name__icontains = weapon)
        weapon_name = weapons[0].skin_name.split("|")[0]
        context = {'weapons': weapons, 'weapon_name': weapon_name}
        return render(request, 'existing_skins.html', context)
    

def current_rifle(request,weapon, pk):
        weapon_from_database = Weapon.objects.filter(id=pk, skin_name__icontains = weapon)
        
        if len(weapon_from_database) == 0:
            return HttpResponseNotFound("Item not found!")  
        context = {'weapon': weapon_from_database.get()}
        return render(request, 'current_rifle.html', context)


def sell_item(request):
     context = {}
     return render(request, "sell.html", context)