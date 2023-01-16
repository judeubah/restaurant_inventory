Project requirements

General Requirements:
* "An application that will keep track of how much food they have throughout the day"
    * Inventory of different ingredients. Their available quantity and prices per unit - "Ingredients" model
    * List of the restaurants -Menu Items- and price for each item. "MenuItems" model
    * List of ingredients that each menu item requires (RecipeRequirements). "RecipeRequirements" model
    * A log of all purchases made at the restaurant. "Purchases" model

Project stakeholder has asked for the following:
1. Ability to enter new recipes, along with their recipe requirements, and how much that menu item costs
2. In inventory they should be able to add:
    1. Name of an ingredient
    2. price per unit
    3. how much of the item is available
3. 
    * Should be able to add in a customer purchase of a menu item. 
    * When a customer makes a purchase the inventory should be modified accordingly
    * Time of purchase should be recorded too

Key points:
* Ingredients, recipies and purchase data should be stored in db
    * Should be rendered via views.
* Need endpoints (forms) for creation
    * New recipes
    * New customer purchases
* Get: All to be rendered in views
    * Info of total cost of inventory
    * Purchases that have been made
    * Hows much inventory needs a re-stock
