from django.contrib import auth
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, PostForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'posts': posts})


def UserSignupView(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # register user
            form.save()
            messages.success(
                request, f'Your account has been created! You are now able to log in')
            # redirect to login
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/signup.html', {'form': form})


def UserLoginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)
            messages.success(
                request, f'You have been successfully logged in as {user.username}')
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, f'You have been successfully logged out')
    return redirect('home')


@login_required
def create_post_view(request):
    if request.method == 'POST':
        form = PostForm(data=request.POST)
        if form.is_valid():
            # log the user in
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(
                request, f'New post has been created')
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'user/createpost.html', {'form': form})
