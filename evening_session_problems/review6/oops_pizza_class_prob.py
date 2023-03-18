"""
# Create a Pizza class with the attributes order_number and ingredients (which is given as a list). Only the
# ingredients will be given as input.
# You should also make it so that its possible to choose a ready made pizza flavour rather than typing out the
# ingredients manually! As well as creating this Pizza class, hard-code the following pizza flavours.
# Name  Ingredients
# hawaiian  ham, pineapple
# meat_festival beef, meatball, bacon
# garden_feast  spinach, olives, mushroom
# Examples
# p1 = Pizza(["bacon", "parmesan", "ham"])    # order 1
# p2 = Pizza.garden_feast()                  # order 2
# p1.ingredients ➞ ["bacon", "parmesan", "ham"]
# ===========================================================
# p2.ingredients ➞ ["spinach", "olives", "mushroom"]
# p1.order_number ➞ 1
# p2.order_number ➞ 2
"""

class Pizza:
    order_number = 0

    def __init__(self, ingredients):
        self.ingredients = ingredients

    def garden_feast(self):
        pass

# class Pizza:
#     # Hard-coded pizza flavors
#     flavors = {
#         "hawaiian": ["mozzarella", "ham", "pineapple"],
#         "meat_feast": ['beef', 'meatball', "bacon"],
#         "garden_feast": ['spinach', 'olives', 'mushroom'],
#
#     }
#
#     def __init__(self, ingredients):
#
#         self.order_number = Pizza.get_next_order_number()
#         if isinstance(ingredients, str):
#             self.ingredients = Pizza.flavors.get(ingredients, [])
#         else:
#             self.ingredients = ingredients
#
#     @staticmethod
#     def get_next_order_number():
#         if not hasattr(Pizza, "last_order_number"):
#             Pizza.last_order_number = 0
#         Pizza.last_order_number += 1
#         return Pizza.last_order_number
#
# p1 = Pizza(["tomato sauce", "mozzarella", "pepperoni"])
# print(p1.order_number)  # Output: 1
# print(p1.ingredients)   # Output: ['tomato sauce', 'mozzarella', 'pepperoni']
#
# # Create a pizza by specifying a flavor
# p2 = Pizza("vegetarian")
# print(p2.order_number)  # Output: 2
# print(p2.ingredients)   # Output: ['tomato sauce', 'mozzarella', 'mushrooms', 'peppers', 'onions']







if __name__ == '__main__':
    ingre = ["bacon", "parmesan", "ham"]
    p1 = Pizza(ingre)
    print(p1.ingredients)