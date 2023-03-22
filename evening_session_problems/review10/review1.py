# TODO: Create a function that takes in n, a, b and returns the number of positive values raised to the nth power that
#  lie in the range [a, b], inclusive.
#   # Examples
#   power_ranger(2, 49, 65) ➞ 2
#   # 2 squares (n^2) lie between 49 and 65, 49 (7^2) and 64 (8^2)
#   power_ranger(3, 1, 27) ➞ 3
#   # 3 cubes (n^3) lie between 1 and 27, 1 (1^3), 8 (2^3) and 27 (3^3)
#   power_ranger(10, 1, 5) ➞ 1
#   # 1 value raised to the 10th power lies between 1 and 5, 1 (1^10)
#   power_ranger(5, 31, 33) ➞ 1
#   power_ranger(4, 250, 1300) ➞ 3
import math


def power_ranger(n, a, b):
    count = 0
    for i in range(a, b):
        c = math.sqrt(i)
        # b = int(math.sqrt(i))
        # d = math.pow(b, n)
        # print(b)
        # print(a)
        if i == c**n:
            count += 1
    return count


# Jack and Jill are twins. When they are 10 years of age, Jack leaves earth in his spaceship bound for Altair IV, some
# 17 light-years distant. Though not equipped with warp drive, Jack's ship is still capable of attaining near light
# speed. When he returns to earth he finds that Jill has grown to adulthood while he, Jack, remains a young boy.
# Implement a function that has as it's arguments: The twins' age at the time of Jack's departure, the distance in
# light-years to the destination star, and the speed of Jack's ship as a fraction of the speed of light. The function
# will return Jack's age and Jill's age at the time of Jack's return to earth, rounded to the nearest tenth of a year.
# The math is simple enough for 10-year-old Jack to understand. See Resources for help.
# Examples
# twins(20, 10, 0.4) ➞ "Jack's age is 65.8, Jill's age is 70.0"
# twins(20, 10, 0.8) ➞ "Jack's age is 35.0, Jill's age is 45.0"
# twins(10, 16.73, 0.999) ➞ "Jack's age is 11.5, Jill's age is 43.5"
# # The Altair IV trip.

def twins(age, distance, speed):
    # light_year_distant = 17
    # jack_age =  age +
    pass


# Create a function that creates a box based on dimension n.
# Examples
# make_box(5) ➞ [
#   "#####",
#   "#   #",
#   "#   #",
#   "#   #",
#   "#####"
# ]
# make_box(3) ➞ [
#   "###",
#   "# #",
#   "###"
# ]
#
# make_box(2) ➞ [
#   "##",
#   "##"
# ]
#
# make_box(1) ➞ [
#     "#"
# ]

def make_box(num):
    for i in range(num):
        for j in range(num):
            if i==0 or i==num-1 or j==0 or j==num-1:
                print("#", end="")
            else:
                print(" ", end="")
        print()





# A city skyline can be represented as a 2-D list with 1s representing buildings. In the example below, the height of
# the tallest building is 4 (second-most right column).
#
# [[0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 1, 0],
# [0, 0, 1, 0, 1, 0],
# [0, 1, 1, 1, 1, 0],
# [1, 1, 1, 1, 1, 1]]
# Create a function that takes a skyline (2-D list of 0's and 1's) and returns the height of the tallest skyscraper.
# Examples
# tallest_skyscraper([
#   [0, 0, 0, 0],
#   [0, 1, 0, 0],
#   [0, 1, 1, 0],
#   [1, 1, 1, 1]
# ]) ➞ 3
#
# tallest_skyscraper([
#   [0, 1, 0, 0],
#   [0, 1, 0, 0],
#   [0, 1, 1, 0],
#   [1, 1, 1, 1]
# ]) ➞ 4
#
# tallest_skyscraper([
#   [0, 0, 0, 0],
#   [0, 0, 0, 0],
#   [1, 1, 1, 0],
#   [1, 1, 1, 1]
# ]) ➞ 2


def tallest_skyscraper(list_of_lists):
    a = []
    for sub_list in list_of_lists:
        for i, num in enumerate(sub_list):
            if num == 1:
                ind = sub_list.index(num)
                a.append(ind)
    print(a)




if __name__ == '__main__':
    # print(power_ranger(2, 49, 65))
    # print( power_ranger(3, 1, 27))
    # print(power_ranger(10, 1, 5))

    # print(twins(20, 10, 0.4))

    make_box(5)
    print()
    make_box(3)
    print()
    make_box(2)
    print()
    make_box(1)

    # tallest_skyscraper([
    #   [0, 0, 0, 0],
    #   [0, 1, 0, 0],
    #   [0, 1, 1, 0],
    #   [1, 1, 1, 1]
    # ])

