from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Weapon
from django.http import HttpResponseNotFound, HttpResponse
from .forms import WeaponForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def loginPage(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist!")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        
        else:
            messages.error(request, "Username or Password does not exist!")


    context = {'page': page}
    return render(request, 'login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "An error occurred during registration")
    return render(request, 'login_register.html', {'form': form})


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    weapons = Weapon.objects.filter(skin_name__icontains = q)
    context = {'weapons': weapons}
    return render(request, 'existing_skins.html', context)

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
        context = {'weapons': weapons, 'weapon_name': weapon}
        return render(request, 'existing_skins.html', context)
    

def current_rifle(request,weapon, pk):
        weapon_from_database = Weapon.objects.filter(id=pk, skin_name__icontains = weapon)
        
        if len(weapon_from_database) == 0:
            return HttpResponseNotFound("Item not found!")  
        context = {'weapon': weapon_from_database.get()}
        return render(request, 'current_rifle.html', context)

@login_required(login_url='/login')
def sell_item(request):
    form = WeaponForm()
    if request.method == 'POST':
        form = WeaponForm(request.POST)
        if form.is_valid():
             form.save()
             return redirect('home')

    context = {'form': form}
    return render(request, 'sell.html', context)


@login_required(login_url='/login')
def update_item(request, pk):
    weapon = Weapon.objects.get(id=pk)
    form = WeaponForm(instance=weapon)

    if request.user != weapon.seller:
        return HttpResponse('Cannot edit this Ad!')

    if request.method == 'POST':
        form = WeaponForm(request.POST, instance=weapon)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'sell.html', context)


@login_required(login_url='/login')
def delete_item(request, pk):
    item = Weapon.objects.get(id=pk)

    if request.user != item.seller:
        return HttpResponse('Cannot edit this Ad!')
    
    if request.method == 'POST':
        item.delete()
        return redirect('home')
    return render(request, 'delete.html', {'obj':item})