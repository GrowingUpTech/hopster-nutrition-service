from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import FoodNutrition
from .serializers import FoodNutritionSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = []
    return(Response(routes))

@api_view(['GET'])
def get_all_food(food):
    all_food = FoodNutrition.objects.all()
    serializer = FoodNutritionSerializer(all_food, many=True)
    return Response(serializer.data)
