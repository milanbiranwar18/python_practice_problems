# "In mathematics, interval is the difference between the largest number and the smallest number in a list.
#
# To illustrate:
#
# A = (3, 5, 7, 23, 11, 42, 80)
#
# Interval of A = 80 - 3 = 77
#
# Examole
# face_interval([1, 2, 5, 8, 3, 9]) ➞ "":)""
# # List interval is equal to one of the other elements.
#
# face_interval([5, 2, 8, 3, 11]) ➞ "":(""
# # List interval is not among the other elements.
#
# face_interval(""bruh"") ➞ "":/""
# # ""bruh"" is not a list. It's string."
import random


def face_interval(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
    b = a[-1] - a[0]
    return b



# "John is playing a dice game. The rules are as follows.
#
# Roll two dice.
# Add the numbers on the dice together.
# Add the total to your overall score.
# Repeat this for three rounds.
# But if you roll DOUBLES, your score is instantly wiped to 0 and your game ends immediately!
#
# Create a function that takes in a list of tuples as input, and return John's score after his game has ended.
#
# Examples
# dice_game([(1, 2), (3, 4), (5, 6)]) ➞ 21
#
# dice_game([(1, 1), (5, 6), (6, 4)]) ➞ 0
#
# dice_game([(4, 5), (4, 5), (4, 5)]) ➞ 27


def roll_dice(a):
    for i in a:
        for j in i:
            pass


# "Given a list of integers representing the color of each sock, determine how many pairs of socks with matching
# colors there are. For example, there are 7 socks with colors [1, 2, 1, 2, 1, 3, 2]. There is one pair of color 1 and
# one of color 2. There are three odd socks left, one of each color. The number of pairs is 2.
#
# Create a function that returns an integer representing the number of matching pairs of socks that are available.
#
# Examples
# sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20]) ➞ 3


def matching_pair(a):
    b = []
    for i in a:
        if a.count(i) != 1:
            b.append(i)
    # c = 0
    # for j in a:
    #     for k in b:
    #         if j==k:
    #             b.count(k)

    c = set(b)
    d = list(c)

    e = 0
    for j in c:
        for k in b:
            if j==k:
                d = b.count(k)
                e+=d

    # c = 0
    # for j in b:
    #     if b.count(j)!=1:
    #         c += 1
    # print(c)










# "Create a function that takes a string containing integers as well as other characters and return the sum of the
# negative integers only.
#
# Examples
# negative_sum("" - 12
# 13 % 14 & -11
# "") ➞ -23
# # -12 + -11 = -23
#
# negative_sum(""
# 22
# 13 % 14 & -11 - 22
# 13
# 12
# "") ➞ -33
# # -11 + -22 = -33"


#  07
# "Create a function that finds a target number in a list of prime numbers. Implement a binary search algorithm in your
# function. The target number will be from 2 through 97. If the target is prime then return ""yes"" else return ""no"".
#
# Examples
# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
#
# is_prime(primes, 3) ➞ ""
# yes
# ""
#
# is_prime(primes, 4) ➞ ""
# no
# ""
#
# is_prime(primes, 67) ➞ ""
# yes
# ""
#
# is_prime(primes, 36) ➞ ""
# no
# """



if __name__ == '__main__':
    # a = [1, 2, 5, 8, 3, 9]
    # b = [5, 2, 8, 3, 11]
    # c = face_interval(a)
    # if c in a:
    #     print(c, "  ", ":)")
    # else:
    #     print(":(")

    # print(face_interval(b))

    # roll_dice()

    a = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    print(matching_pair(a))



