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
