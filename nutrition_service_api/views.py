from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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
        '/nutrition/api/v1/food/',
        '/nutrition/api/v1/food/all/',
        '/nutrition/api/v1/food/<str:tag>/'
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
    try: 
        all_food = FoodNutrition.objects.all()
        
        if not all_food.exists():
            return Response({'message': 'No food items found.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = FoodNutritionSerializer(all_food, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_food_by_tag(request, tag):
    """
    Retrieve all food items from the giving tag in database.

    Args:
        request (Request): The request object.
        tag (String): A string of tag type

    Returns:
        Response: A response object containing the serialized list of all food items in each tag request.
    """
    try:
        foods = FoodNutrition.objects.filter(food_tag=tag)
        if not foods.exists():
            return Response({'message': 'No food items found for the given tag.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = FoodNutritionSerializer(foods, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
