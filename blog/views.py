from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from blog.models import Post

# Create your views here.
def blog_view(request, cat_name=None, author_username=None):
    posts = Post.objects.filter(status=1)
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    if author_username:
        posts = posts.filter(author__username=author_username)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(Post, pk=pid)
    context = {'post': post}
    return render(request, 'blog/blog-single.html', context)

def test(request):
    return render(request, 'test.html')

def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if search_get := request.GET.get('s'):
            posts = posts.filter(content__contains=search_get)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)