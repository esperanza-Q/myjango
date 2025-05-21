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


#여기는 테스트 용도 리스트 함수
# 나중에 지울 거임
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'test_recipe_list.html', {'recipes': recipes})
