from blog.models import Category, Blog
from django import forms

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ("name",)

    def save(self, commit=True):
        category = super().save(commit=False)
        if commit:
            category.save()
        return category