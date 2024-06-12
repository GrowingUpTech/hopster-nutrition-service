from django.db import models

class FoodNutrition(models.Model):
    food_name           = models.CharField(null=False, max_length=255)
    food_kcal           = models.FloatField(default=0)
    food_carbohydrates  = models.FloatField(default=0)
    food_protien        = models.FloatField(default=0)
    food_fat            = models.FloatField(default=0)

    def __str__(self) -> str:
        return self.food_name