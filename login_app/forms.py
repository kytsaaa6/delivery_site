from django import forms


class PersonForm(forms.Form):
    name = forms.CharField(label='name', max_length=30)
    birth = forms.DateField(label='birth')
    age = forms.IntegerField(label='age')