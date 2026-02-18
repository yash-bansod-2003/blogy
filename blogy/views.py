from django.shortcuts import render

from blog.models import Blog, Category
from blogy.forms import RegisterForm

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