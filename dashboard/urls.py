

from django.urls import include, path

from dashboard.views import dashboard, dashboard_categories, dashboard_posts, dashboard_categories_add, dashboard_categories_edit

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("categories/", dashboard_categories, name="dashboard_categories"),
    path("categories/add/", dashboard_categories_add, name="dashboard_categories_add"),
    path("categories/edit/<int:category_id>/", dashboard_categories_edit, name="dashboard_categories_edit"),
    path("posts/", dashboard_posts, name="dashboard_posts")
]