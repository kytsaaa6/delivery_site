from django import forms
from .models import Store,Menu

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name','address','text']

class MenuForm(forms.ModelForm):
    class Meta:
        medel = Menu
        fields = ['count']