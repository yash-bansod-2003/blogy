from django.urls import path

from .views import blog_detail

urlpatterns = [
    # Blog app URL patterns will go here
    path("<slug:slug>", blog_detail, name="blog_detail"),
]
