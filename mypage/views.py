from django.shortcuts import render, redirect, get_object_or_404

from recipe.models import Recipe
from .models import Scrap, ScrapRecipe, UserIngredient
from .forms import IngredientForm

# Create your views here.
def mypage(request):
    return render(request, 'test_mypage.html')

def myref(request):
    ingredients = UserIngredient.objects.filter(user = request.user)
    return render(request, 'test_myref.html', {'ingredients':ingredients})

def ing_add(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if request.POST['icon'] == "meat":
            icon = 'img/재료아이콘/고기테스트.png'
        elif request.POST['icon'] == "vegetable":
            icon = 'img/재료아이콘/채소테스트.png'
        elif request.POST['icon'] == "fruit":
            icon = 'img/재료아이콘/과일테스트.png'
        else:
            icon = 'img/재료아이콘/소스테스트.png'

        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.icon = icon
            ingredient.user = request.user
            ingredient.expiration_date = request.POST['expiration_date']
            ingredient.save()
        
        return redirect('mypage:myref')
        
    else:
        ingredients = UserIngredient.objects.filter(user = request.user)
        form = IngredientForm()
        return render(request, 'test_ing_add.html', {'form':form, 'ingredients':ingredients})
    
def ing_detail(request, ing_id):
    ing = get_object_or_404(UserIngredient, id=ing_id)
    ingredients = UserIngredient.objects.filter(user = request.user)
    return render(request, 'test_ing_detail.html', {'ing':ing, 'ingredients':ingredients})

def ing_delete(request, ing_id):
    ing = get_object_or_404(UserIngredient, id=ing_id)
    ing.delete()
    return redirect('mypage:myref')

def ing_update(request, ing_id):
    ing = get_object_or_404(UserIngredient, id=ing_id)
    ingredients = UserIngredient.objects.filter(user = request.user)
    if request.method == 'POST':
        form=IngredientForm(request.POST, instance=ing)
        
        if request.POST['icon'] == "meat":
            icon = 'img/재료아이콘/고기테스트.png'
        elif request.POST['icon'] == "vegetable":
            icon = 'img/재료아이콘/채소테스트.png'
        elif request.POST['icon'] == "fruit":
            icon = 'img/재료아이콘/과일테스트.png'
        else:
            icon = 'img/재료아이콘/소스테스트.png'
        
        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.icon = icon
            ingredient.user = request.user
            ingredient.expiration_date = request.POST['expiration_date']
            ingredient.save()
            
        return redirect('mypage:myref')
    else:
        form=IngredientForm(instance=ing)
        context = {
            'form':form,
            'ingredients':ingredients,
            'expiration_date': ing.expiration_date,
            'icon' : ing.icon
        }
        print(ing.icon)
        return render(request, 'test_ing_update.html', context)
    
    
#🔽스크랩 파트
    
def scrap(request):
    scraps = Scrap.objects.filter(user=request.user)
    return render(request, 'test_scrap.html', {'scraps':scraps})

def scrap_addFolder(request):
    scraps = Scrap.objects.filter(user=request.user)
    if request.method == 'POST':
        name=request.POST['scrapName']
        
        if not Scrap.objects.filter(user=request.user, name=name):
            Scrap.objects.create(
                user = request.user,
                name = name
            )
            return redirect('mypage:scrap')
        return render(request, 'test_scrap_add.html', {'scraps':scraps})
    else:
        return render(request, 'test_scrap_add.html', {'scraps':scraps})
    
def scrap_deleteFolder(request):
    scraps = Scrap.objects.filter(user=request.user)
    if request.method=='POST':
        scrap_ids = request.POST.getlist('scrap_ids')
        Scrap.objects.filter(id__in=scrap_ids, user=request.user).delete()
        return redirect('mypage:scrap')
    else:
        return render(request, 'test_scrap_delete.html', {'scraps':scraps})
        
def scrap_detail(request, scrap_id):
    scraps = Scrap.objects.filter(user=request.user)
    scrap = get_object_or_404(Scrap, id=scrap_id)
    scrapRecipes = ScrapRecipe.objects.filter(scrap=scrap)
    context = {
        'scraps':scraps,
        'selected_scrap' : scrap,
        'scrapRecipes' : scrapRecipes
    }
    return render(request, 'test_scrap_detail.html', context)
    
# def add_to_scrap_folder(request, recipe_id, scrap_id):
#     scrap = Scrap.objects.get(id=scrap_id, user=request.user)
#     recipe = Recipe.objects.get(id=recipe_id)

#     # 이미 스크랩되어 있는지 확인
#     if not ScrapRecipe.objects.filter(scrap=scrap, recipe=recipe).exists():
#         ScrapRecipe.objects.create(scrap=scrap, recipe=recipe)
    
