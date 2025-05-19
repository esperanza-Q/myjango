from django.shortcuts import render, redirect, get_object_or_404
from .models import UserIngredient
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
        form = IngredientForm()
        return render(request, 'test_ing_add.html', {'form':form})