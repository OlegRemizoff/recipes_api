from django.urls import path
from .views import RecipeAPIView, DetailRecipeAPIView



urlpatterns = [
    path('<int:pk>/', DetailRecipeAPIView.as_view()),
    path('', RecipeAPIView.as_view(), name='home'),

    

]