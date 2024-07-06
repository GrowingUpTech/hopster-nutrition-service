from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import FoodNutrition
from .serializers import FoodNutritionSerializer
from .utils.decorators import cache_response

@api_view(['GET'])
def getRoutes(request):
    """
    Retrieve all available API routes.

    Args:
        request (Request): The request object.

    Returns:
        Response: A response object containing the list of available routes.
    """
    routes = [
        '/nutrition_service_api/api/',
        '/nutrition_service_api/api/get_all_food'
    ]
    return(Response(routes))

@api_view(['GET'])
@cache_response(timeout=60 * 15, cache_key_prefix='all_food_', invalidate_cache=False)
def get_all_food(request):
    """
    Retrieve all food items from the database.

    Args:
        request (Request): The request object.

    Returns:
        Response: A response object containing the serialized list of all food items.
    """
    all_food = FoodNutrition.objects.all()
    serializer = FoodNutritionSerializer(all_food, many=True)
    return Response(serializer.data)
