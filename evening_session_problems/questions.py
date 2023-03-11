# TODO : Que = 1
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply
# X + II. The number 27 is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
# Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same
# principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.
# Example 1:
#
# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:
#
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:
#
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.





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
