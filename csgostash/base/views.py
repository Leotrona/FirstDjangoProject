from django.shortcuts import render
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
