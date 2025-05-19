from django import forms
from .models import UserIngredient

class IngredientForm(forms.ModelForm):
    class Meta:
        model = UserIngredient
        fields = ('name', 'amounts', 'unit')