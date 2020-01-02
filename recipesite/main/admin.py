from django.contrib import admin
from .models import Recipe
from tinymce.widgets import TinyMCE
from django.db import models

class RecipeAdmin(admin.ModelAdmin):
    fields = ["recipe_title",
              "recipe_published",
              "recipe_content"]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }    

admin.site.register(Recipe,RecipeAdmin)
# Register your models here.
