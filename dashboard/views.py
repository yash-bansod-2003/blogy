from django.shortcuts import render
from blog.models import Category, Blog

def dashboard(request):
    categories_count = Category.objects.count()
    posts_count = Blog.objects.count()
    context = {
        "categories_count": categories_count,
        "posts_count": posts_count
    }
    return render(request, "dashboard/dashboard.html", context)