class Recipe:
    
    name = ""
    cooking_lvl = 1
    cooking_time = 1
    ingredients = []
    description = ""
    recipe_type = ""
    def __init__(self, name = None, cooking_lvl = None, cooking_time = None, ingredients = None, description = None, recipe_type = None):
        
        if type(name) != str:
            print("Recipe name need to be a str")
            exit()
        if type(cooking_lvl) != int:
            print("Recipe cooking level need to be an int")
            exit()
        if type(cooking_time) != int:
            print("Recipe cooking time need to be an int")
            exit()
        if type(ingredients) != list:
            print("Recipe ingredients need to be a list")
            exit()
        if type(description) != str and type(description) != None:
            print("Recipe description need to be a str")
            exit()
        if type(recipe_type) != str:
            print("Recipe description need to be a str")
        if len(name) < 1:
            print("Recipe name cannot be empty")
            exit()
        if cooking_lvl < 1 or cooking_lvl > 5:
            print("Recipe cooking level needs to be in range(1, 5)")
            exit()
        if len(ingredients) == 0:
            print("Recipe ingredients list cannot be empty")
            exit()
        for i in range(len(ingredients)):
            if type(ingredients[i]) != str:
                print(ingredients[i])
                print("Recipe ingredients values needs to be a str")
                exit()
        if recipe_type != "starter" and recipe_type != "lunch" and recipe_type != "dessert":
            print("Recipe type can only be set to \'starter\', \'lunch\' or \'dessert\'")
            exit()
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
    
    def __str__(self):

        txt = self.name + "\n\n"
        txt += "    Cooking level: " + str(self.cooking_lvl) + "\n"
        txt += "    Cooking time: " + str(self.cooking_time) + "\n"
        txt += "    Ingredients:\n"
        for i in self.ingredients:
            txt += "     - " + i + "\n"
        txt += "    Description: " + self.description + "\n"
        txt += "    Recipe type: " + self.recipe_type + "\n"
        return txt

#test = Recipe("Soupe", 2, 10, ["eau", "tomates", "epices"], "Bonne soupe", "starter")

#print(str(test))