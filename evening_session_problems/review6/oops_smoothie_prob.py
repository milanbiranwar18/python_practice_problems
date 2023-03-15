# Create a class Smoothie and do the following:
# Create an instance attribute called ingredients.
# Create a get_cost method which calculates the total cost of the ingredients used to make the smoothie.
# Create a get_price method which returns the number from get_cost plus the number from get_cost multiplied by 1.5.
# Round to two decimal places.
# Create a get_name method which gets the ingredients and puts them in alphabetical order into a nice descriptive
# sentence. If there are multiple ingredients, add the word "Fusion" to the end but otherwise, add "Smoothie". Remember
# to change "-berries" to "-berry". See the examples below.
# Strawberries($1.50), Banana($0.50), Mango($2.50), Blueberries($1.00), Raspberries($1.00), Apple($1.75), Pineapple($3.50)
# Examples
# s1 = Smoothie(["Banana"])
# s1.ingredients ➞ ["Banana"], s1.get_cost() ➞ "$0.50", s1.get_price() ➞ "$1.25", s1.get_name() ➞ "Banana Smoothie"
# s2 = Smoothie(["Raspberries", "Strawberries", "Blueberries"])
# s2.ingredients ➞ ["Raspberries", "Strawberries", "Blueberries"]
# s2.get_cost() ➞ "$3.50", s2.get_price() ➞ "$8.75"
#
# s2.get_name() ➞ "Blueberry Raspberry Strawberry Fusion"


class Smoothie:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def get_price(self):
        a_dict = {'Strawberries': 1.50, 'Banana': 0.50, 'Mango': 2.50, 'Blueberries': 1.00,
                  'Raspberries': 1.00, 'Apple': 1.75, 'Pineapple': 3.50}

        total_price_ingre = 0
        for ingredient in self.ingredients:
            if ingredient in a_dict.keys():
                ingre_price = ingredient * 1.5
                total_price_ingre += ingre_price
        return total_price_ingre

    def get_cost(self):
        return self.get_price()

    def get_name(self):
        # a_str = ''
        b_str = 'Fusion'
        c_str = 'Smoothie'
        # for ingredient in self.ingredients:
        #     a_str = a_str + " " + ingredient
        #
        a_str = " ".join(self.ingredients)

        if len(self.ingredients) == 1:
            a_str = a_str + " " + c_str
        else:
            a_str = a_str + " " + b_str
        return a_str


if __name__ == '__main__':
    s1 = Smoothie(["Banana"])
    s1.get_name()

    s2 = Smoothie(["Raspberries", "Strawberries", "Blueberries"])
    print(s2.get_name())

    # s2.get_price()
