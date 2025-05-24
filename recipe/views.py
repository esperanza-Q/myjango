from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm
from .models import Recipe, RecipeIngredient

@login_required
def create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.writer = request.user
            recipe.save()
            
            # 다중 재료 처리
            # recipe_ingredient.js에서 설정한 리스트 이름입니다!
            names = request.POST.getlist('ingredients_name[]')
            amounts = request.POST.getlist('ingredients_amount[]')
            units = request.POST.getlist('ingredients_unit[]')
            
            
            for name, amount, unit in zip(names, amounts, units):
                # name, amount, unit 리스트에서 인덱스가 동일한 애들끼리 묶어 튜플 생성!
                # 재료마다 객체 생성 및 저장
                RecipeIngredient.objects.create(
                    recipe_id=recipe,
                    name=name,
                    amount=amount,
                    unit=unit
                )
            
            return redirect('recipe:detail', recipe_id=recipe.id)
        else:
            context = {
                'form': form,
                # ingredientForm은 따로 안 쓰므로 빼거나 빈 값 전달
            }
            return render(request, 'recipe_write.html', context)
    else:
        form = RecipeForm()
        return render(request, 'recipe_write.html', {'form':form})


def detail(request, recipe_id):
    recipe = Recipe.objects.filter(pk=recipe_id).first()
    # recipe_ing = RecipeIngredient.objects.filter(pk=recipe_id)
    # pk=recipe_id는 pk 자체 즉, 재료의 id가 recipe_id와 같은 값 하나만 가져오는 거!
    
    recipe_ing = RecipeIngredient.objects.filter(recipe_id=recipe_id)
    # 데베에 외래키로 이용된 recipe_id가 같은 재료들 전부를 불러옴

    context = {
        'recipe' : recipe,
        'recipe_ing' : recipe_ing
    }
    
    return render(request, 'recipe_detail.html', context)


#여기는 테스트 용도 리스트 함수
# 나중에 지울 거임
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'test_recipe_list.html', {'recipes': recipes})
