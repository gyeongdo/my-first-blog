from django.shortcuts import get_object_or_404,redirect, render
from django.utils import timezone
from .models import Post
from .forms import PostForm


def post_list(request):
    # 모든 디비에 저장된 정보를 불러옴
    qs = Post.objects.all()
    # less than equals lte <= 지금 시간 (당연히 만든시간이 지금보다 작겟지)
    qs = qs.filter(published_date__lte = timezone.now())
    # 시간순으로 출력인데 -는 
    qs = qs.order_by('-published_date')

    return render(request, 'blog/post_list.html',{
        'post_list' : qs,
    })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {
        'post' : post,
    })

def post_year(request):
    #post = get_object_or_404(Post)
    #return redirect('blog/post_year.html')    
    return render(request, 'blog/post_year.html')

def post_new(request):
    form_class = PostForm
    form = form_class(request.POST or None)
    if request.method == 'POST':
        # form = form_class(request.POST, request.Files)
        if form.is_valid():
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('post_detail', post.pk)
        else:
            form = PostForm
    return render(request, 'blog/post_edit.html', {
        'form': form, 
    })

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    form_class = PostForm
    # instance=post 수정버튼을 누를때 기존글을 전달해주는 기능
    form = form_class(request.POST or None, instance=post)
    if request.method == 'POST':
        if form.is_valid():
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('post_detail', post.pk)
        else:
            form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', {
        'form': form,
    })
