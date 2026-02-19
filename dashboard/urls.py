

from django.urls import include, path

from dashboard.views import dashboard, dashboard_categories, dashboard_posts

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("categories/", dashboard_categories, name="dashboard_categories"),
    path("posts/", dashboard_posts, name="dashboard_posts")
]