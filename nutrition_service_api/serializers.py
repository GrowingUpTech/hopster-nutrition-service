from rest_framework import serializers
from .models import FoodNutrition

class FoodNutritionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodNutrition
        fields = '__all__'