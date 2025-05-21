from pyexpat.errors import messages
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

def scrap_select_view(request, recipe_id):
    scraps = Scrap.objects.filter(user=request.user)  # 사용자별 스크랩 필터
    recipe = get_object_or_404(Recipe, id=recipe_id)

    # 이 레시피가 포함된 스크랩 ID 목록
    scrap_ids_with_recipe = ScrapRecipe.objects.filter(recipe=recipe, scrap__in=scraps).values_list('scrap_id', flat=True)
    
    context = {
        'scraps': scraps,
        'recipe': recipe,
        'scrap_ids_with_recipe': list(scrap_ids_with_recipe),
    }
    
    return render(request, 'test_scrap_select.html', context)
    
def add_to_scrap_folder(request, recipe_id):
    
    if request.method == "POST":
        recipe = get_object_or_404(Recipe, id=recipe_id)
        user_scraps = Scrap.objects.filter(user=request.user)
        selected_scrap_ids = request.POST.getlist('scrap_ids')  # ['1', '3', ...]

        # 기존에 연결되어 있던 스크랩 목록
        existing_scrap_ids = ScrapRecipe.objects.filter(recipe=recipe, scrap__in=user_scraps).values_list('scrap_id', flat=True)

        # 새로 추가해야 할 scrap_id들
        to_add = set(selected_scrap_ids) - set(map(str, existing_scrap_ids))
        # 제거해야 할 scrap_id들
        to_remove = set(map(str, existing_scrap_ids)) - set(selected_scrap_ids)
        
        # 추가
        for scrap_id in to_add:
            scrap = get_object_or_404(Scrap, id=scrap_id, user=request.user)
            ScrapRecipe.objects.create(scrap=scrap, recipe=recipe)

        # 삭제
        for scrap_id in to_remove:
            ScrapRecipe.objects.filter(scrap_id=scrap_id, recipe=recipe).delete()

        # messages.success(request, "스크랩 정보가 업데이트되었습니다.")
        return redirect('recipe:detail', recipe_id=recipe.id)

    return redirect('recipe:detail', recipe_id=recipe_id)
    