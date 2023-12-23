from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from blog.models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.forms import CommentForm
from django.contrib import messages

# Create your views here.
def blog_view(request, cat_name=None, author_username=None, tag_name=None):
    posts = Post.objects.filter(status=1)
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    if author_username:
        posts = posts.filter(author__username=author_username)
    if tag_name:
        posts = posts.filter(tags__name__in=tag_name)

    posts = Paginator(posts, 3)
    
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request, pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your message has been sent successfully.')
        else:
            messages.add_message(request, messages.ERROR, 'There is an error.Try again later.')
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts, pk=pid)
    comments = Comment.objects.filter(post=post.id, approved=True)
    form = CommentForm()
    context = {'post': post, 'comments':comments, 'form':form}
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