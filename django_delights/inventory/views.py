from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from . models import Ingredient, MenuItem, Purchase, RecipeRequirement
from django.urls import reverse_lazy
import itertools


def home(request):
    purchases= Purchase.objects.all()    
    def trial():
        return 'lol'
    cost = getCostPurchases(purchases)
    revenue=getRevenue(purchases)
    context={"name": "Jude", "func":trial, "cost": cost, "revenue":revenue, "profit": round(revenue-cost,2), "purchases":purchases}
    return render(request, "inventory/index.html", context)

def getRevenue(purchases):
    return round(sum([purchase.menu_item.price for purchase in purchases]),2)

def getCostPurchases(purchases):    
    extract = lambda items: [item.ingredient.unit_price* item.quantity for item in items]
    ingreds=[extract(purchase.menu_item.reciperequirement_set.all()) for purchase in purchases]
    return round(sum(list(itertools.chain(*ingreds))),2)


class PurchasesList(ListView):
    model=Purchase
    template_name=""

class IngredientsList(ListView):
    model=Ingredient
    template_name= "inventory/ingredients.html"

class MenuItemsList(ListView):
    model=MenuItem
    template_name="inventory/menu.html"

def delete_ingredient(request, ingred_id):
    try:
        ingredient=Ingredient.objects.get(pk=ingred_id)
    except Ingredient.DoesNotExist:
        raise Http404("Ingredient does not exist")
    else:
        ingredient.delete()
        return redirect("ingredients")

def delete_menu_item(menu_id):
    try:
        menu_item=MenuItem.objects.get(pk=menu_id)
    except MenuItem.DoesNotExist:
        raise Http404("Menu item does not exist")
    else: 
        menu_item.delete()
        return redirect('menu_items')