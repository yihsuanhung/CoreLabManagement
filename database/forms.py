from django import forms
from .models import Person, PI, Staff, Card

class PersonForm(forms.ModelForm):
    # myfield = forms.CharField(widget=forms.TextInput(attrs={'class' : 'myfieldclass'}))
    class Meta:
        model = Person
        fields = '__all__'
        widgets = {
            'access_card': forms.CheckboxInput(attrs={'class': 'myfieldclass'}),
            'uid': forms.Select(attrs={'class': 'select'}),
        }


class PIForm(forms.ModelForm):
    class Meta:
        model = PI
        fields = '__all__'
        widgets = {
            'uid': forms.Select(attrs={'class': 'select'}),
        }


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = '__all__'
