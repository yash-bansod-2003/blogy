

from django.urls import include, path

from dashboard.views import dashboard, dashboard_categories, dashboard_posts, dashboard_categories_add

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("categories/", dashboard_categories, name="dashboard_categories"),
    path("categories/add/", dashboard_categories_add, name="dashboard_categories_add"),
    path("posts/", dashboard_posts, name="dashboard_posts")
]