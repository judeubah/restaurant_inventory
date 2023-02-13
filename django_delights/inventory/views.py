from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from . models import Ingredient, MenuItem, Purchase, RecipeRequirement
from django.urls import reverse_lazy
import itertools
from .forms import MenuItemCreateForm, PurchaseCreateForm


def home(request):
    return render(request, "inventory/index.html", panel_context())

def getRevenue(purchases):
    return round(sum([purchase.menu_item.price for purchase in purchases]),2)

def getCostPurchases(purchases):    
    extract = lambda items: [item.ingredient.unit_price* item.quantity for item in items]
    ingreds=[extract(purchase.menu_item.reciperequirement_set.all()) for purchase in purchases]
    return round(sum(list(itertools.chain(*ingreds))),2)

def panel_context():
    purchases= Purchase.objects.all() 
    recent_purchases=purchases.order_by('-timestamp')[:3]

    menuItems = MenuItem.objects.all()

    popular_items=[    
    {
        "item":item,
        "num_purchases":len(item.purchase_set.all())
    } 
    for item in menuItems][:5]
    popular_items.sort(key=lambda food: food['num_purchases'], reverse=True)
    
    
     
    cost = getCostPurchases(purchases)
    revenue=getRevenue(purchases)
    generic_info=[
        {"name":"Number of Purchases", "value":len(purchases)},
        {"name":"Operating Costs", "value":cost},
        {"name":"Proft", "value":round(revenue-cost,2)}
    ]
    context={"name": "Jude", "generic_info":generic_info, "purchases":purchases, "recent_purchases":recent_purchases, "popular_items":popular_items}
    return context

class PurchasesList(ListView):
    model=Purchase
    template_name="inventory/purchases.html"
    extra_context=panel_context()

class IngredientsList(ListView):
    model=Ingredient
    template_name= "inventory/ingredients.html"
    extra_context=panel_context()

class MenuItemsList(ListView):
    model=MenuItem
    template_name="inventory/menu.html"
    extra_context=panel_context()

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

class NewMenuItem(CreateView):
    model=MenuItem
    template_name="forms/new_menu_item.html"
    form_class = MenuItemCreateForm
    extra_context=panel_context()
