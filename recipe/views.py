from django.shortcuts import render, redirect, get_object_or_404
from .models import RecipeWrite, RecipeImage
from .forms import RecipeWriteForm

# Create your views here.

def recipe_write(request):
    if request.method == 'POST':
        form = RecipeWriteForm(request.POST)
        if form.is_valid():
            recipe_post = form.save(commit=False)
            # form의 데이터를 바탕으로 모델 인스턴스를 생성하긴 하나, 아직 데베에 저장되진 않음.
            # post 는 데이터 베이스에 저장되지 않았다.
            # 위 내용을 commit=False가 수행해준다.
            
            recipe_post.recipe_writer = request.user
            # 여기서 user는 (django에서) 현재 글 작성을 요청한 사람을 뜻함
            
            if recipe_post is None:
                return render(request, 'test_recipe_write.html', {'recipe_form': form, 'error': '내용을 작성하세요.'})
            
            recipe_post.save()
            # .save()를 호출해야 최종적으로 데베에 저장됨.
            
            RecipeImage.objects.create(write=recipe_post, recipe_image=request.FILES['recipe_image']) 
            #이미지는 필수 1개로만 제한할 거라, for 문 돌리지 않았습니다.
            #여기서 'recipe_image'는 test_recipe_write.html의 input - name 중 하나
                                
            return redirect('recipe:recipe_detail', recipe_post_id=recipe_post.id )
        return render(request, 'test_recipe_write.html',  {'form': form, 'error': '내용을 작성하세요.'})      
    else:
        form = RecipeWriteForm() #현재 상황인 request가 빈 값이니 아예 새로운 폼을 불러옴.
        return render(request, 'test_recipe_write.html', {'form':form})
    
def recipe_detail(request, recipe_post_id):
    recipe_post=RecipeWrite.objects.filter(pk=recipe_post_id).first()
    recipe_image=RecipeImage.objects.filter(write_id=recipe_post_id).first()
   
    return render(request, 'test_recipe_detail.html', {'recipe_post':recipe_post, 'recipe_image':recipe_image})
    

# 삭제 및 수정 기능 구현

def recipe_delete(request, recipe_post_id):
    recipe_post = get_object_or_404(RecipeWrite, pk=recipe_post_id)
    recipe_image = get_object_or_404(RecipeImage, write_id=recipe_post_id)
    recipe_post.delete()
    recipe_image.delete()
    
    #recipe_write에서 recipe_post란 변수에 게시글이 새로 작성되고
    #그 게시글의 id를 가져와서 recipe_delete를 실행시킴. 다른 것도 마찬가지~
    
    return redirect('home:home')

def recipe_update(request, recipe_post_id):
    recipe_post = get_object_or_404(RecipeWrite, pk=recipe_post_id)
    recipe_image = RecipeImage.objects.filter(write=recipe_post).first()
    
    if request.method == "POST":
        recipeForm = RecipeWriteForm(request.POST, request.FILES, instance=recipe_post)
        
        if recipeForm.is_valid():
            recipe_post = recipeForm.save()
            #img는 이 필드에 들어가 있지 않으니, title과 content 변경했을 때 저장

        if 'recipe_image' in request.FILES:
        #여기서 recipe_image - html:name 값
        #recipe_image에 새 이미지 파일이 업로드됐을 때 true.
        #현재 요청에서 새로 업로드된 파일만 포함. (사용자가 새로운 이미지를 선택했는지 여부 확인)
        
            if recipe_image:  # 기존 이미지가 있으면 삭제
                recipe_image.delete()
            #RecipeImage의 write 필드는 외래키라서 pk로 받으면 안 됨.
            #get() : 반드시 하나의 객체만 있을 때, filter(): 여러 개의 객체가 있을 가능성 O
            
            # 새 이미지 저장
            RecipeImage.objects.create(write=recipe_post, recipe_image=request.FILES['recipe_image']) 
            
            # recipe_image.recipe_image = request.FILES['recipe_image']
            #HTML 폼에서 name="recipe_image"인 파일을 받아서 
            #그 파일을 recipe_image 모델의 recipe_image 필드에 할당
            # recipe_image.save()
            #create부분으로 객체 생성해서 저장하는 건 충분하다.
        
        return redirect('recipe:recipe_detail', recipe_post_id=recipe_post.id)
        #수정 후 다시 수정 페이지를 렌더링하는 거 X, 상세 페이지로 redirect해야 됨.
        #redirect는 새로고침 시 데이터가 다시 전송되는 문제도 방지 가능
        #redirect엔 URL 받기
    
    else:
        recipe_form = RecipeWriteForm(instance=recipe_post)
        context = {
            'recipe_form' : recipe_form,
            'recipe_post' : recipe_post,
            'recipe_post_id' : recipe_post_id,
            'recipe_image' : recipe_image
        }
        
        return render(request, 'test_recipe_update.html', context)