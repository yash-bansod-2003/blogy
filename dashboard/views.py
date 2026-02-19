from django.shortcuts import render
from blog.models import Category, Blog
from django.contrib.auth.decorators import login_required
from dashboard.forms import CategoryForm

@login_required(login_url='login')
def dashboard(request):
    categories_count = Category.objects.count()
    posts_count = Blog.objects.count()
    context = {
        "categories_count": categories_count,
        "posts_count": posts_count
    }
    return render(request, "dashboard/dashboard.html", context)

def dashboard_categories(request):
    categories = Category.objects.all()
    context = {
        "categories": categories
    }
    return render(request, "dashboard/dashboard_categories.html", context)

def dashboard_categories_add(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CategoryForm()
    context = {
        "form": form
    }
    return render(request, "dashboard/dashboard_categories_add.html", context)

def dashboard_posts(request):
    posts = Blog.objects.all()
    context = {
        "posts": posts
    }
    return render(request, "dashboard/dashboard_posts.html", context)