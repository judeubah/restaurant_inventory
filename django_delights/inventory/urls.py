from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.home, name="home"),
    path("ingredient/all", views.IngredientsList.as_view(), name="ingredients"),
    path("ingredient/<int:ingred_id>/delete/", views.delete_ingredient, name="delete_ingredient"),
    path("menu", views.MenuItemsList.as_view(), name="menu_items"),
    path("ingredient/<int:menu_id>/delete/", views.delete_menu_item, name="delete_menu_item"),
]