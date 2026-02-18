from django.urls import path

from .views import blog_detail, blogs_by_category

urlpatterns = [
    # Blog app URL patterns will go here
    path("<slug:slug>", blog_detail, name="blog_detail"),
    path("category/<int:category_id>/", blogs_by_category, name="blogs_by_category"),
]
