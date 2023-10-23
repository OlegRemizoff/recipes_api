from rest_framework import serializers
from .models import Recipe




class RecipeSerializer(serializers.ModelSerializer):
    # ingredients = serializers.SlugRelatedField(slug_field='name', many=True, read_only=True)
    # ingredients = serializers.StringRelatedField(many=True)
    # hello_world = serializers.ReadOnlyField()
    
    class Meta:
        model = Recipe
        # fields = ['id', 'name', 'description', 'ingredients', "cooking_steps", "total_time"]
        fields = "__all__"
    




