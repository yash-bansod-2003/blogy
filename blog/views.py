from django.shortcuts import get_object_or_404, render

from .models import Blog, Category


# Create your views here.
def blog_detail(request, slug):
    categories = Category.objects.all()
    blog = get_object_or_404(Blog, slug=slug, status="published")
    context = {
        "categories": categories,
        "blog": blog,
    }
    return render(request, "blog/blog_detail.html", context)

def blogs_by_category(request, category_id):
    categories = Category.objects.all()
    category = get_object_or_404(Category, id=category_id)
    blogs = Blog.objects.filter(category=category, status="published")
    context = {
        "categories": categories,
        "category": category,
        "posts": blogs,
    }
    return render(request, "blog/blogs_by_category.html", context)