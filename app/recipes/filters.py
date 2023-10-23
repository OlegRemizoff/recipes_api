from django_filters import FilterSet, CharFilter
from .models import Recipe


class RecipeFilter(FilterSet):
    ingredients = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Recipe
        fields = ['ingredients', 'cooking_time']