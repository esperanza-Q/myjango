from django import forms
from .models import RecipeWrite

class RecipeWriteForm(forms.ModelForm):
    class Meta:
        model = RecipeWrite
        fields = [ 'recipe_title', 'recipe_content']