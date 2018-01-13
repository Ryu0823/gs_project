from django.utils import timezone
from .models import Post, Message
from django.shortcuts import render, get_object_or_404, redirect
from .forms import FormPost, FormMessage
from django.contrib.auth import views as auth_views
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'chatty/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    messages = Message.objects.filter(postId=pk).order_by('id')
    form = FormMessage(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            message = form.save(commit=False)
            message.postId = Post.objects.get(id=pk)
            message.order = messages.count() + 1
            message.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = FormMessage()
    return render(request, 'chatty/post_detail.html', {
        'post': post,
        'messages': messages,
        'form': form,
        })

def post_new(request):
    if request.method == 'POST':
        form = FormPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = FormPost()
    return render(request, 'chatty/post_new.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = FormPost(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = FormPost(instance=post)
    return render(request, 'chatty/post_edit.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(request, 'chatty/signup.html', {'form': form})
