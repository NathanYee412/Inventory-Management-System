from django import forms
from .models import *

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = ('type' , 'partNumber', 'price' , 'status' , 'issues' , 'user' , 'location')

class DesktopForm(forms.ModelForm):
    class Meta:
        model = Desktop
        fields = ('type' , 'partNumber', 'price' , 'status' , 'issues' , 'user' , 'location')


class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = ('type' , 'partNumber', 'price' , 'status' , 'issues' , 'user' , 'location')

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ('type' , 'partNumber', 'price' , 'status' , 'issues' , 'user' , 'location')
