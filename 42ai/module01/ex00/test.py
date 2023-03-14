from book import Book
from recipe import Recipe

my_book = Book()
test = Recipe("Soupe", 2, 10, ["eau", "tomates", "epices"], "Bonne soupe", "starter")
test2 = Recipe("Cookie", 2, 5, ["Chocolat", "Sucre", "Oeufs", "Farine"], "Cookie moelleux", "dessert")
x = 2
print(str(test2))
print()
print(str(my_book.last_update))
my_book.add_recipe(test)
print(str(my_book.last_update))
my_book.add_recipe(x)
print(str(my_book.last_update))
my_book.add_recipe(test2)
print(str(my_book.last_update))

my_book.get_recipes_by_types("starter")

my_book.get_recipe_by_name("Soupe")