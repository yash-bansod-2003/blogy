from django.contrib import admin

from .models import Blog, Category


class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "is_featured", "created_at")
    list_filter = ("status", "is_featured", "category")
    list_editable = ("status", "is_featured")
    search_fields = ("title", "description", "content")
    # if we want to search by related model fields so we use double underscore
    # search_fields = ("category__name")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "created_at"
    ordering = ("-created_at",)


# Register your models here.
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
