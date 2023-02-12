from django.db import models
import datetime
from django.utils import timezone
import calendar

# Create your models here.
class Ingredient(models.Model):
    name=models.CharField(max_length=200)
    quantity=models.DecimalField(default=0, max_digits=4, decimal_places=1)
    unit_price=models.DecimalField(max_digits=6, decimal_places=2)
    mililitre='mL';litre="L";teaspoon="tsp.";tablespoon="tbl.";fluid_ounce="fl oz"
    cup="c"; pint="p";gallon="gal";miligram="mg";gram="g";kilogram="kg"; pounds="lbs"
    ounce="oz"; whole_unit="unit"
    UNIT_CHOICES=[(mililitre, "Mililitre"), (litre, "Litre"), (teaspoon,"Teaspoon"),
    (tablespoon,"Tablespoon"),(fluid_ounce,"Fluid Ounce"), (cup, "Cup"), (pint, "Pint"),
    (gallon,"Gallon"),(miligram,"Miligram"), (gram,"Gram"),(kilogram, "Kilogran"),
    (pounds, "Pounds"),(ounce, "Ounce"), (whole_unit,"Individual Unit")]
    unit=models.CharField(max_length=5, choices=UNIT_CHOICES)

    class Meta:
        ordering=['name']

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return "/ingredient/all"

class MenuItem(models.Model):
    title=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=6, decimal_places=2)
    star_rating=models.IntegerField(default=3, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    
    class Meta:
        ordering=['star_rating']
    def __str__(self):
        return f"{self.title}"
    
    def iterable_stars(self):
        return range(self.star_rating)

class RecipeRequirement(models.Model):
    menu_item=models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient=models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity=models.DecimalField(max_digits=4, default=0, decimal_places=1)

    

    def __str__(self):
        return f"{self.ingredient} for {self.menu_item}"

class Purchase(models.Model):
    menu_item=models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp=models.DateTimeField()

    def __str__(self):
        return f"{self.menu_item}: {self.timestamp}"

    def simplified_time(self):
        month=self.timestamp.month
        return self.timestamp.strftime(f"%d-{calendar.month_name[month]}-%Y")
    
    class Meta:
        ordering=["timestamp"]