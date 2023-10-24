import os
from random import randint, choice
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")  # Замените на имя вашего проекта

import django
django.setup()

from mimesis import Generic
from recipes.models import Recipe

ingredient_list = [
    "Мука", "Сахар", "Молоко", "Яйцо", "Соль", "Перец", "Масло", "Лук", "Чеснок",
    "Помидор", "Огурец", "Брокколи", "Картофель", "Морковь", "Курица", "Говядина",
    "Свинина", "Рыба", "Креветки", "Сыр", "Спагетти", "Рис", "Грибы", "Перец чили",
    "Имбирь", "Лимон", "Петрушка", "Базилик", "Куркума", "Паприка", "Капуста", "Апельсин",
    "Банан", "Ананас", "Малина", "Шоколад", "Мед", "Ваниль", "Какао", "Корица", "Орехи",
    "Сухофрукты",
]


def generate_recipe_data():
    generic = Generic('ru')

    for _ in range(10):  
        name = generic.food.dish()
        description = generic.text.text()
        ingredients = [{choice(ingredient_list): randint(3, 8)} for _ in range(5)]
        cooking_steps = [{"time": randint(1, 30), "description": generic.text.text()}, {"time": randint(1, 30), "description": generic.text.text()}, {"time": randint(1, 30), "description": generic.text.text()}]


        recipe = Recipe.objects.create(name=name, description=description, 
                                       ingredients=ingredients, cooking_steps= cooking_steps)
        recipe.save()

if __name__ == '__main__':
    print("Заполняю базу данных...")
    generate_recipe_data()
    print("База данных успешно заполнена.")