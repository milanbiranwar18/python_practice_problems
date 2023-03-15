import math

"""

# Your task is to create a class to handle paginated content in a website. A pagination is used to divide long lists of content in a series of pages.
# Example
# The pagination class will accept 2 parameters:
# items (default: []): A list of contents to paginate.
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

"""

class Pagination():
    def __init__(self, items, page_size):
        self.items = items
        self.page_size = page_size

    def first_page(self):
        a_list = []
        for i in range(len(self.items)):
            if i < 4:
                a_list.append(self.items[i])

    def second_page(self):
        a_list = []
        for i in range(len(self.items)):
            if i==4 or i>4 and i < 8:
                a_list.append(self.items[i])

    def third_page(self):
        a_list = []
        for i in range(len(self.items)):
            if i == 8 or i > 8 and i < 12:
                a_list.append(self.items[i])

    def fourth_page(self):
        a_list = []
        for i in range(len(self.items)):
            if i == 12 or i > 12 and i < 16:
                a_list.append(self.items[i])

    def fifth_page(self):
        a_list = []
        for i in range(len(self.items)):
            if i == 16 or i > 16 and i < 20:
                a_list.append(self.items[i])

    def six_page(self):
        a_list = []
        for i in range(len(self.items)):
            if i == 20 or i > 20 and i < 24:
                a_list.append(self.items[i])

    def last_page(self):
        a_list = []
        for i in range(len(self.items)):
            if i == 24 or i > 24 and i <= 26:
                a_list.append(self.items[i])

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
#####################################################################

class Paginator:
    def __init__(self, items, items_per_page):
        self.items = items
        self.items_per_page = items_per_page

    def get_page(self, page_number):
        start_index = (page_number - 1) * self.items_per_page
        end_index = start_index + self.items_per_page
        return self.items[start_index:end_index]

    def num_pages(self):
        return math.ceil(len(self.items) / self.items_per_page)

    def has_previous(self, page_number):
        return page_number > 1

    def has_next(self, page_number):
        return page_number < self.num_pages()

    def previous_page_number(self, page_number):
        if self.has_previous(page_number):
            return page_number - 1
        else:
            return None

    def next_page_number(self, page_number):
        if self.has_next(page_number):
            return page_number + 1
        else:
            return None


if __name__ == '__main__':
    # alphabet_list = "abcdefghijklmnopqrstuvwxyz"
    # n = 4
    # p = Pagination(alphabet_list, n)
    # p.first_page()
    # p.second_page()
    # p.third_page()
    # p.fourth_page()
    # p.fifth_page()
    # p.six_page()
    # p.last_page()

    items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    paginator = Paginator(items, 3)

    # Get the first page
    page_number = 1
    page_items = paginator.get_page(page_number)
    print(page_items)  # [1, 2, 3]

    # Get the second page
    page_number = 2
    page_items = paginator.get_page(page_number)
    print(page_items)  # [4, 5, 6]

    # Get the third page
    page_number = 3
    page_items = paginator.get_page(page_number)
    print(page_items)  # [7, 8, 9]

    # Check if there's a previous page
    has_previous_page = paginator.has_previous(page_number)
    print(has_previous_page)  # True

    # Check if there's a next page
    has_next_page = paginator.has_next(page_number)
    print(has_next_page)  # False

    # Get the previous page number
    previous_page_number = paginator.previous_page_number(page_number)
    print(previous_page_number)  # 2

    # Get the next page number
    next_page_number = paginator.next_page_number(page_number)
    print(next_page_number)  # None

    # Get the total number of pages
    num_pages = paginator.num_pages()
    print(num_pages)  # 4

