from django.shortcuts import render, redirect

from blog.models import Blog, Category
from blogy.forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

def home(request):
    categories = Category.objects.all()
    featured_blogs = Blog.objects.filter(is_featured=True, status="published").order_by(
        "-created_at"
    )[:5]
    blogs = Blog.objects.filter(status="published").order_by("-created_at")[:10]
    context = {
        "categories": categories,
        "featured_blogs": featured_blogs,
        "blogs": blogs,
    }
    return render(request, "home.html", context)


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "home.html")
    else:
        form = RegisterForm()
    return render(request, "auth/register.html", {"form": form})

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            print(username, password)

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return render(request, "home.html")
    form = AuthenticationForm()
    return render(request, "auth/login.html", {"form": form})

def logout(request):
    auth.logout(request)
    return redirect("home")    