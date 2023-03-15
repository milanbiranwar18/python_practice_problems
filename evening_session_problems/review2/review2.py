import calendar
import datetime

"""
# "Create a function to perform basic arithmetic operations that includes addition, subtraction, multiplication and
# division on a string number (e.g. ""12 + 24"" or ""23 - 21"" or ""12 // 12"" or ""12 * 21"").
# Here, we have 1 followed by a space, operator followed by another space and 2. For the challenge, we are going to
# have only two numbers between 1 valid operator. The return value should be a number.
# eval() is not allowed. In case of division, whenever the second number equals ""0"" return
"""


def arithmatic_operation(a_string):
    a = a_string.split()

    for i in a:
        if i == '+':
            b = int(a[0]) + int(a[2])
            return b
        elif i == '-':
            b = int(a[0]) - int(a[2])
            return b
        elif i == '*':
            b = int(a[0]) * int(a[2])
            return b
        elif i == '//':
            b = int(a[0]) // int(a[2])
            return b


"""
# "A number is said to be Disarium if the sum of its digits raised to their respective positions is the number itself.
# Create a function that determines whether a number is a Disarium or not.
# Examples
# is_disarium(75) ➞ False
# # 7^1 + 5^2 = 7 + 25 = 32
# is_disarium(135) ➞ True
# # 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135
# is_disarium(544) ➞ False
# is_disarium(518) ➞ True
# is_disarium(466) ➞ False
# is_disarium(8) ➞ True
# "
"""


def is_disarium_num(num):
    num_string = str(num)
    a = 1
    b = 0
    for i in num_string:
        c = int(i) ** a
        b += c
        a += 1
    if b == num:
        return True
    return False


"""
# "If a person traveled up a hill for 18mins at 20mph and then traveled back down the same path at 60mph then their
# average speed traveled was 30mph.
# Write a function that returns the average speed traveled given an uphill time, uphill rate and a downhill rate.
# Uphill time is given in minutes. Return the rate as an integer (mph). No rounding is necessary.
# Examples
# ave_spd(18, 20, 60) ➞ 30
# ave_spd(30, 10, 30) ➞ 15
# ave_spd(30, 8, 24) ➞ 12"
"""


def average_speed(a, b, c):
    time_to_up_hill = a
    speed_up_hill = b
    speed_back_hill = c
    time_to_convert_hrs = time_to_up_hill / 60
    distance = speed_up_hill * time_to_convert_hrs
    doun_speed_time = distance / speed_back_hill
    total_time = time_to_convert_hrs + doun_speed_time
    total_distance = 2 * distance
    avg_speed = total_distance / total_time
    return avg_speed


"""
# "Given the month and year as numbers, return whether that month contains a Friday 13th.
# Examples
# has_friday_13(3, 2020) ➞ True
# has_friday_13(10, 2017) ➞ True
# has_friday_13(1, 1985) ➞ False"
"""


def checking_day(y, m, d):
    cal = calendar.month(y, m)
    # def day_fun():
    #     pass

    # cal1 = calendar.weekday(y, m, d)
    # print(cal1)


def has_friday_13(month, year):
    d = datetime.date(year, month, 13)
    return d.weekday() == 4


"""
# "Create a function which returns how many Friday 13ths there are in a given year.
# Examples
# how_unlucky(2020) ➞ 2
# how_unlucky(2026) ➞ 3
# how_unlucky(2016) ➞ 1"
"""


def num_fri_in_year(year):
    count = 0
    for month in range(1, 13):
        obj = datetime.date(year, month, 13)
        if obj.weekday == 4:
            count += 1

    return count


"""
# "Create a function that takes a list lst and a number n and returns a list of two integers whose product is that of 
# the number n.
# Examples
# two_product([1, 2, 3, 4, 13, 5], 39) ➞ [3, 13]
# two_product([11, 2, 7, 3, 5, 0], 55) ➞ [5, 11]
# two_product([100, 12, 4, 1, 2], 15) ➞ None"
"""


def two_product(a_list):
    b_list = []
    for i in a_list:
        for j in a_list:
            if a_list.index(i) == a_list.index(j):
                continue
            obj = i * j
            if obj == 55:
                b_list.append(i)
                b_list.append(j)
    res = set(b_list)
    c_list = list(res)
    return c_list[::-1]


"""
# "In the class Employee, implement the instance attributes as firstname, lastname and salary.
# Create the method from_string() which parses a string containing these attributes and assigns them to the correct
# properties. Properties will be separated by a dash.
# Examples
# emp1 = Employee(""Mary"", ""Sue"", 60000)
# emp2 = Employee.from_string(""John-Smith-55000"")
# emp1.firstname ➞ ""Mary""
# emp1.salary ➞ 60000
# emp2.firstname ➞ ""John""
# emp2.salary ➞ 55000"
"""


class Employee():
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    @staticmethod
    def from_string(a_sting):
        a_list = a_sting.split("-")
        obj = Employee(*a_list)
        return obj

    @classmethod
    def from_string1(cls, emp_str):
        firstname, lastname, salary = emp_str.split('-')
        return cls(firstname, lastname, int(salary))


"""
# "Your task is to create a class to handle paginated content in a website. A pagination is used to divide long lists
# of content in a series of pages.
# Example
# The pagination class will accept 2 parameters:
# items (default: []): A list of contents to paginate.
# pageSize (default: 10): The amount of items to show in each page.
# So for example we could initialize our pagination like this:
# alphabetList = ""abcdefghijklmnopqrstuvwxyz"".split('')
# p = Pagination(alphabetList, 4)
# And then use the meth
# Shuvam18:19
# alphabetList = "abcdefghijklmnopqrstuvwxyz".split('')
# p = Pagination(alphabetList, 4)
# And then use the method getVisibleItems to show the contents of the paginated list.
# p.getVisibleItems() # ["a", "b", "c", "d"]
# You will have to implement various methods to go through the pages such as:
# prevPage
# nextPage
# firstPage
# lastPage
# goToPage
# Here's a continuation of the example above using nextPage and lastPage:
# p.nextPage()
# p.getVisibleItems()
# # ["e", "f", "g", "h"]
# p.lastPage()
# p.lastPage()
# p.getVisibleItems()
# # ["y", "z"]
"""


class Pagiantion():
    def __init__(self, items, page_size):
        self.items = items
        self.page_size = page_size

    def getVisibleItems(self):
        pass


if __name__ == '__main__':
    # a_string = "12 + 24"
    # a_string = "12 // 12"
    # a = arithmatic_operation(a_string)
    # print(a)

    # num = 466
    # res_num = is_disarium_num(num)
    # print(res_num)

    # average_speed(18, 20, 60)

    # checking_day(2020, 3)

    # print(has_friday_13(3, 2020))

    # obj = num_fri_in_year(2020)
    # print(obj)

    b = [11, 2, 7, 3, 5, 0]
    print(two_product(b))

    # emp1 = Employee("Mary", "Sue", 60000)
    # print(emp1.firstname)
    # print(emp1.salary)
    # emp2 = Employee.from_string("John-Smith-55000")
    # print(emp2.firstname)
    # print(emp2.salary)
    # emp3 = Employee.from_string1("John-Smith-55000")
    # print(emp3.firstname)
    # print(emp3.salary)
