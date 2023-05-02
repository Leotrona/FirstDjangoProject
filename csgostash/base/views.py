from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Weapon
from django.http import HttpResponseNotFound, HttpResponse
from .forms import WeaponForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

WEAPON_TYPES = {
    'rifles': ['AK-47', 'M4A4', 'AWP', 'M4A1-S', 'GALIL', 'AUG'],
    'knives': ['BAYONET', 'KARAMBIT', 'M9-BAYONET', 'BUTTERFLY', 'SKELETON', 'FLIP'],
    'pistols': ['DEAGLE', 'DUALS', 'GLOCK', 'P250', 'TEC9', 'USP-S'],
    'smg': ['BIZON', 'MAC10', 'MP5', 'MP7', 'MP9', 'UMP45'],
    'heavy': ['M249', 'MAG7', 'NEGEV', 'NOVA', 'SAWED', 'XM1014'],
    'gloves': ['BROKEN', 'DRIVER', 'HAND', 'MOTO', 'SPECIALIST', 'SPORT'],
    'cases': ['DREAMS', 'FALCHON', 'OPERATION', 'REVOLUTION', 'SOUVENIR', 'WEAPON'],
    'stickers': ['ASTRALIS', 'CERQ', 'DEVICE', 'NIKO', 'NIP', 'S1MPLE'],
}


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
            login(request, user)
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


def weapons(request, type):

    weapons = WEAPON_TYPES.get(type)
    context = {'weapons': weapons, 'type': type}
    return render(request, 'weapons_type.html', context)


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    weapons = Weapon.objects.filter(skin_name__icontains=q)
    context = {'weapons': weapons}
    return render(request, 'existing_skins.html', context)


def existing_skins(request, weapon, type):

        if weapon == 'a':
            return HttpResponseNotFound("Item not found!")

        weapons = Weapon.objects.filter(skin_name__icontains=weapon)
        context = {'weapons': weapons, 'weapon_name': weapon}
        return render(request, 'existing_skins.html', context)


def current_rifle(request, weapon, pk, type):
        weapon_from_database = Weapon.objects.filter(
            id=pk, skin_name__icontains=weapon)

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
            full_name = form.fields['skin_name']
            name = str(full_name).split("|")[0].lower()
            for type in WEAPON_TYPES:
                 if name in WEAPON_TYPES.get(type):
                     form.fields['weapon_type'] = type
                     break
            weapon = form.save(commit=False)
            weapon.seller = request.user
            weapon.save()
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