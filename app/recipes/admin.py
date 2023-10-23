from django.contrib import admin
from .models import Recipe







@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "cooking_time"]
    list_display_links = ["id", "name"]
    search_fields = ["name", "ingredients"]

