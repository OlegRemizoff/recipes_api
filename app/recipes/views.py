from rest_framework import generics
from  django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import Recipe
from .serializers import RecipeSerializer
from .filters import RecipeFilter




class RecipeAPIView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = RecipeFilter
    ordering_fields = ['cooking_time']
    
    # def get_queryset(self):
    #     queryset = Recipe.objects.all()
    #     q = self.request.query_params.get('ingredients')
    #     print(q)
    #     if q is not None:
    #         queryset = queryset.filter(ingredients=q)
    #         # print(queryset)
    #     return queryset

    

class DetailRecipeAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    












# class RecipeAPIView(generics.ListCreateAPIView):
#     queryset = Recipe.objects.all()
#     serializer_class = RecipeSerializer





















# from rest_framework.decorators import action
# from rest_framework.response import Response
# from rest_framework import status

    # @action(detail=False, methods=['POST'])
    # def create_recipe(self, request):
    #     recipe_data = request.data
    #     ingredients_data = recipe_data.pop('ingredients', [])
        
    #     recipe_serializer = RecipeSerializer(data=recipe_data)
    #     if recipe_serializer.is_valid():
    #         recipe = recipe_serializer.save()

    #         for ingredient_data in ingredients_data:
    #             ingredient, created = Ingredient.objects.get_or_create(**ingredient_data)
    #             recipe.ingredients.add(ingredient)

    #         return Response(recipe_serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(recipe_serializer.errors, status=status.HTTP_400_BAD_REQUEST)