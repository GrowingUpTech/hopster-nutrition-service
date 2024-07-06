from django.urls import path
from . import views

urlpatterns = [
    path('nutrition/api/v1/food/', views.getRoutes, name="routes"),
    path('nutrition/api/v1/food/all/', views.get_all_food),
    path('nutrition/api/v1/food/<str:tag>/', views.get_food_by_tag)
]