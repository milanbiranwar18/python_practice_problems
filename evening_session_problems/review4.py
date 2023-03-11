# Your task is to create a class to handle paginated content in a website. A pagination is used to divide long lists of content in a series of pages.
#
# Example
#
# The pagination class will accept 2 parameters:
#
# items (default: []): A list of contents to paginate.
#
# pageSize (default: 10): The amount of items to show in each page.
#
# So for example we could initialize our pagination like this:
#
# alphabetList = ""abcdefghijklmnopqrstuvwxyz"".split('')
#
# p = Pagination(alphabetList, 4)
# And then use the method getVisibleItems to show the contents of the paginated list.
#
# p.getVisibleItems() # ["a", "b", "c", "d"]
# You will have to implement various methods to go through the pages such as:
#
# prevPage
# nextPage
# firstPage
# lastPage
# goToPage
# Here's a continuation of the example above using nextPage and lastPage:
#
# p.nextPage()
#
# p.getVisibleItems()
# # ["e", "f", "g", "h"]
#
# p.lastPage()
#
# p.getVisibleItems()
# # ["y", "z"]


class Pagination():
    def __init__(self, items, page_size):
        self.items = items
        self.page_size = page_size

    def first_page(self):
        a_list = []
        for i in range(len(self.items)):
            if i < 4:
                a_list.append(self.items[i])
        print(a_list)

    def second_page(self):
        a_list = []
        for i in range(len(self.items)):
            if i==4 or i>4 and i < 8:
                a_list.append(self.items[i])

        print(a_list)

    def third_page(self):
        a_list = []
        for i in range(len(self.items)):
            if i == 8 or i > 8 and i < 12:
                a_list.append(self.items[i])

        print(a_list)

    def fourth_page(self):
        a_list = []
        for i in range(len(self.items)):
            if i == 12 or i > 12 and i < 16:
                a_list.append(self.items[i])

        print(a_list)

    def fifth_page(self):
        a_list = []
        for i in range(len(self.items)):
            if i == 16 or i > 16 and i < 20:
                a_list.append(self.items[i])

        print(a_list)

    def six_page(self):
        a_list = []
        for i in range(len(self.items)):
            if i == 20 or i > 20 and i < 24:
                a_list.append(self.items[i])

        print(a_list)

    def last_page(self):
        a_list = []
        for i in range(len(self.items)):
            if i == 24 or i > 24 and i <= 26:
                a_list.append(self.items[i])

        print(a_list)



    def prev_page(self):
        pass

    def next_page(self):
        pass

    def go_to_page(self):

        pass

    method_list = [fifth_page(), second_page(), third_page(), fourth_page(), first_page(), six_page(), last_page()]
    def get_visible_items(self):

        choice =  input("Enter Method Name")
        while True:
            pass


# "Given a list of people objects, create a function that sorts the list by an attribute name. The attribute to sort by will be given as a string.
#
# The Person class will only include these attributes in the following order:
#
# firstname
# lastname
# age
# Examples
# p1 = Person(""Michael"", ""Smith"", 40)
# p2 = Person(""Alice"", ""Waters"", 21)
# p3 = Person(""Zoey"", ""Jones"", 29)
# people_sort([p1, p2, p3], ""firstname"") ➞ [p2, p1, p3]
# # Alice, Michael, Zoey
# people_sort([p1, p2, p3], "lastname") ➞ [p3, p1, p2]
# # Jones, Smith, Waters
#
# people_sort([p1, p2, p3], "age") ➞ [p2, p3, p1]
# # 21, 29, 40


class Person():
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    @staticmethod
    def sort_attributes():
        p1 = Person("Michael", "Smith", 40)
        p2 = Person("Alice", "Waters", 21)
        p3 = Person('Zoey', 'Jones', 29)

        f_name = []
        f_name.append(p1.firstname)
        f_name.append(p2.firstname)
        f_name.append(p3.firstname)
        sort_f_name = sorted(f_name)
        print(sort_f_name)

        l_name = []
        l_name.append(p1.lastname)
        l_name.append(p2.lastname)
        l_name.append(p3.lastname)
        sort_l_name = sorted(l_name)
        print(sort_l_name)

        age_list = []
        age_list.append(p1.age)
        age_list.append(p2.age)
        age_list.append(p3.age)
        for i in range(len(age_list)-1, 0, -1):
            for i in range(i):
                if age_list[i] > age_list[i+1]:
                    temp = age_list[i]
                    age_list[i] = age_list[i+1]
                    age_list[i + 1] = temp

        print(age_list)




# "Create a class that imitates a select screen. For simplicity, the cursor can only move right!
#
# In the display method, return a string representation of the list, but with square brackets around the currently
# selected element. Also, create the method to_the_right, which moves the cursor one element to the right.
# The cursor should start at index 0.
# Examples
# menu = Menu([1, 2, 3])
# menu.display() ➞ "[[1], 2, 3]"
# menu.to_the_right()
# menu.display() ➞ "[1, [2], 3]"
#
# menu.to_the_right()
# menu.display() ➞ "[1, 2, [3]]"
#
# menu.to_the_right()
# menu.display() ➞ "[[1], 2, 3]"

class Menu():
    def __init__(self, a_list):
        self.a_list = a_list

    def display(self):
        pass

    def to_the_right(self):
        a = '['
        b = ']'
        c = []

        for i in range(len(self.a_list)):
            a_str = str(i)
            c.append(a)
            c.append(a_str)
            c.append(b)






if __name__ == '__main__':
    alphabet_list = "abcdefghijklmnopqrstuvwxyz"
    n = 4
    p = Pagination(alphabet_list, n)
    p.first_page()
    p.second_page()
    p.third_page()
    p.fourth_page()
    p.fifth_page()
    p.six_page()
    p.last_page()


    # Person.sort_attributes()

    # menu = Menu([1, 2, 3])
    # menu.display()
    # menu.to_the_right()

