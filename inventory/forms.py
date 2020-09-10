from django import forms
from .models import *

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = ('type' , 'partNumber', 'price' , 'status' , 'issues' , 'user' , 'location', 'serviceTag')

class DesktopForm(forms.ModelForm):
    class Meta:
        model = Desktop
        fields = ('type' , 'partNumber', 'price' , 'status' , 'issues' , 'user' , 'location', 'serviceTag')


class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = ('type' , 'partNumber', 'price' , 'status' , 'issues' , 'user' , 'location', 'serviceTag')

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ('type' , 'partNumber', 'price' , 'status' , 'issues' , 'user' , 'location', 'serviceTag')
