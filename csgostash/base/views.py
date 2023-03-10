from django.shortcuts import render
from .models import Weapon
# Create your views here.

job_title = [
    "First Job",
    "Second Job",
    "Third Job",
    "Fourth Job",
]


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

def ak47(request):
    try:
        weapons = Weapon.objects.all()
        context = {'weapons': weapons}
        return render(request, 'ak47.html', context)
    except:
        return render("Item not found!")

def current_rifle(request, pk):
    weapon_from_database = Weapon.objects.get(id=pk)
    context = {'weapon': weapon_from_database}
    return render(request, 'current_rifle.html', context)

