from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    ingredients = models.JSONField(default=dict, verbose_name='Ингредиенты', blank=True, null=True)
    cooking_steps = models.JSONField(default=list, verbose_name='Шаги приготовления', blank=True, null=True)
    cooking_time = models.PositiveIntegerField(default=0, verbose_name='Общее время приготовления')

    def get_total_time(self): # функция для подсчета общего количества времени
        total_time = 0
        for step in self.cooking_steps: #"cooking_steps": [{"time": 10, "descript": "Подготовить продукты."  }, {} ]
            if 'time' in step:
                total_time += step['time']
        return total_time


    def hello_world(self):
        return "Hello, World!"


    def save(self, *args, **kwargs): # функция будет вызвана при создании или изменении модели
        self.cooking_time = self.get_total_time() # обновляем поле при помощи нашей функции
        super().save(*args, **kwargs) # обращаемся к базовому классу, чтобы вызвать метод save, а не перезаписать его


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'














# class Recipe(models.Model):
#     name = models.CharField(max_length=250, verbose_name='Название')
#     description = models.TextField(verbose_name='Описание')
#     ingredients = models.ManyToManyField(Ingredient, verbose_name='Ингредиенты')

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = 'Рецепт'
#         verbose_name_plural = 'Рецепты'














# class Recipe(models.Model):
#     title = models.CharField(max_length=255, verbose_name='Название рецепта')
#     description = models.TextField(verbose_name='Описание')
#     ingredients = models.JSONField(verbose_name='Ингредиенты')
#     preparation_steps = models.JSONField(verbose_name='Шаги приготовления')

#     def __str__(self):
#         return self.title

#     class Meta:
#         verbose_name = 'Рецепт'
#         verbose_name_plural = 'Рецепты'