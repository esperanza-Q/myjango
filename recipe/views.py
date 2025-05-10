from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm
from .models import Recipe

@login_required
def create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.writer = request.user
            recipe.save()
            return redirect('recipe:detail', recipe_id=recipe.id)
        else:
            return render(request, 'recipe_write.html', {'form': form})
    else:
        form = RecipeForm()
        return render(request, 'recipe_write.html', {'form': form})
    
    
def detail(request, recipe_id):
    recipe = Recipe.objects.filter(pk=recipe_id).first
    return render(request, 'recipe_detail.html', {'recipe':recipe})
