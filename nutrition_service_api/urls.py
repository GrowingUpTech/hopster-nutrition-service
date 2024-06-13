from django.urls import path
from . import views

urlpatterns = [
    path('nutrition_service_api/api/', views.getRoutes, name="routes"),
    path('nutrition_service_api/api/get_all_food', views.get_all_food)
]