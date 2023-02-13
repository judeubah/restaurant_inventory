from django import forms
from .models import Purchase, MenuItem, Ingredient, RecipeRequirement


#Create
class PurchaseCreateForm(forms.ModelForm):
    class Meta:
        model=Purchase
        fields=("menu_item", "timestamp")

class MenuItemCreateForm(forms.ModelForm):
    class Meta:
        model=MenuItem
        fields=('title', 'price', 'star_rating')


class RecipeRequirementCreateForm(forms.ModelForm):
    class Meta:
        model=RecipeRequirement
        fields=('menu_item', 'ingredient', 'quantity')