cookbook = {}

cookbook['Sandwich'] = {
    'ingredients': ['ham', 'bread', 'cheese'],
    'meal': 'lunch',
    'prep_time': 10
}

cookbook['Cake'] = {
    'ingredients': ['flour', 'sugar', 'eggs'],
    'meal': 'dessert',
    'prep_time': 60
}

cookbook['Salad'] = {
    'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
    'meal': 'lunch',
    'prep_time': 15
}

def print_recipe_list():
    for i in cookbook:
        print(i)
    print()

def print_recipe(name):
    if name in cookbook.keys():
        print(f"Recipe for {name}:")
        print(f" Ingredients list: {cookbook[name]['ingredients']}")
        print(f" To be eaten for {cookbook[name]['meal']}.")
        print(f" Takes {cookbook[name]['prep_time']} minutes of cooking.")
    else:
        print("This recipe does not exist")
    print()

def delete_recipe(name):
    if name in cookbook.keys():
        cookbook.pop(name)
        print(f"Removing {name} recipe from your cookbook")
    else:
        print("This recipe does not exist")
    print()

def add_recipe():
    r_name = input("Enter a name:\n>> ")
    r_ingredients = []
    print("Enter ingredients:")
    while True:
        try:
            line = input(">> ")
            if len(line) == 0:
                break
        except EOFError:
            break
        r_ingredients.append(line)

    r_type = input("Enter a meal type:\n>> ")
    r_time = input("Enter a preparation time:\n>> ")
    cookbook[r_name] = {
        'ingredients' : r_ingredients,
        'meal' : r_type,
        'prep_time' : r_time
    }
    print()

print("Welcome to the Python Cookbook !")
print("List of available option:")
print(" 1: Add a recipe")
print(" 2: Delete a recipe")
print(" 3: Print a recipe")
print(" 4: Print the cookbook")
print(" 5: Quit\n")

while True:
    print("Please select an option:")
    x = input(">> ")
    print()
    if x == '1':
        add_recipe()
    elif x == '2':
        print("Please enter a recipe name to remove it from your cookbook\n")
        name = input(">> ")
        print()
        delete_recipe(name)
    elif x == '3':
        print("Please enter a recipe name to get its details:")
        name = input(">> ")
        print()
        print_recipe(name)
    elif x == '4':
        print_recipe_list()
    elif x == '5':
        break
    else:
        print("Sorry, this option does not exist.")
        print("Welcome to the Python Cookbook !")
        print("List of available option:")
        print(" 1: Add a recipe")
        print(" 2: Delete a recipe")
        print(" 3: Print a recipe")
        print(" 4: Print the cookbook")
        print(" 5: Quit\n")
print("Cookbook closed. Goodbye !")