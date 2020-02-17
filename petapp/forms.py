from django import forms
from .models import PetModel

class PetForm(forms.ModelForm):
    class Meta:
        model = PetModel
        exclude = ['available']
