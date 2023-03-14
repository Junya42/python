import datetime
from recipe import Recipe

class Book:
    
    name = ""
    last_update = None
    creation_date = None
    recipes_list = {}

    def __init__(self, name = "Default"):
        
        self.name = name
        self.creation_date = datetime.datetime.now()
        self.last_update = self.creation_date
        self.recipes_list['starter'] = []
        self.recipes_list['lunch'] = []
        self.recipes_list['dessert'] = []

    def get_recipe_by_name(self, name):

        print("Recipe:")
        for specifier in self.recipes_list:
            for recipe in self.recipes_list[specifier]:
                if recipe.name == name:
                    print(recipe)
                    return recipe
        print("Doesn't exist\n")
        
    
    def get_recipes_by_types(self, recipe_type):

        if recipe_type in self.recipes_list.keys():
            print(recipe_type + " list of recipes:")
            for recipe in self.recipes_list[recipe_type]:
                print(" - " + recipe.name)
        else:
            print("Wrong type of recipe_type")
        print()
        
    def add_recipe(self, recipe):

        if type(recipe) == Recipe:
            self.recipes_list[recipe.recipe_type].append(recipe)
            self.last_update = datetime.datetime.now()
            print("Adding new recipe to book")
        else:
            print("The element you are trying to add to your Book is not a Recipe")
        print()
