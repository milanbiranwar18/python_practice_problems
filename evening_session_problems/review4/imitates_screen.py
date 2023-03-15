"""
# "Create a class that imitates a select screen. For simplicity, the cursor can only move right!
# In the display method, return a string representation of the list, but with square brackets around the currently
# selected element. Also, create the method to_the_right, which moves the cursor one element to the right.
# The cursor should start at index 0.
# Examples
# menu = Menu([1, 2, 3])
# menu.display() ➞ "[[1], 2, 3]"
# menu.to_the_right()
# menu.display() ➞ "[1, [2], 3]"
# menu.to_the_right()
# menu.display() ➞ "[1, 2, [3]]"
# menu.to_the_right()
# menu.display() ➞ "[[1], 2, 3]"
"""

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

    menu = Menu([1, 2, 3])
    menu.display()
    menu.to_the_right()