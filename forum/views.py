from django.shortcuts import render, redirect
from .models import Post, Tema
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'foro/index.html')

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'foro/login.html', {'form': form})

class PostListView(View):
    def get(self, request):
        return redirect('login')  # Siempre redirige al login

class PostCreateView(View):
    def get(self, request):
        return render(request, 'foro/post_create.html') 

    def post(self, request):
        author = request.POST.get('author')
        content = request.POST.get('content')
        post = Post(author=author, content=content)
        post.save()
        return redirect('post_list')  