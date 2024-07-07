from django.db import models
from django.utils.translation import gettext_lazy as _

class FoodNutrition(models.Model):
    class FoodTag(models.TextChoices):
        FRUIT       = 'FR', _('Fruit')
        VEGETABLE   = 'VG', _('Vegetable')
        MEAT        = 'MT', _('Meat')
        DAIRY       = 'DR', _('Dairy')
        GRAIN       = 'GR', _('Grain')
        DRINK       = 'DK', _('Drink')
        OTHER       = 'OT', _('Other')

    food_name           = models.CharField(max_length=255, null=False)
    food_tag            = models.CharField(max_length=2, choices=FoodTag.choices, default=FoodTag.OTHER)
    food_kcal           = models.FloatField(default=0)
    food_carbohydrates  = models.FloatField(default=0)
    food_protein        = models.FloatField(default=0)
    food_fat            = models.FloatField(default=0)

    def __str__(self) -> str:
        return self.food_name