from django.forms import ModelForm
from .models import Weapon

class WeaponForm(ModelForm):
    class Meta:
        model = Weapon
        fields = '__all__'
        exclude = ('weapon_type', 'seller',)