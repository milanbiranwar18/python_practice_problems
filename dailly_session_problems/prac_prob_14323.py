"""
# Given a sorted integer array, find the floor and ceiling of a given number in it. For a given number x, floor(x) is
# the largest integer in the array less than or equal to x, and ceil(x) is the smallest integer in the array greater
# than or equal to x.
#
# The solution should return the (floor, ceil) pair. If the floor or ceil doesn't exist, consider it to be -1.
#
# Input: nums[] = [1, 4, 6, 8, 9], x = 2
# Output: (1, 4)
# Explanation: The floor is 1 and ceil is 4
#
# Input: nums[] = [1, 4, 6, 8, 9], x = 6
# Output: (6, 6)
# Explanation: The floor is 6 and ceil is 6
#
# Input: nums[] = [-2, 0, 1, 3], x = 4
# Output: (3, -1)
# Explanation: The floor is 3 and ceil doesn't exist
"""


def floor_ceil(a_list, x):
    num = -1
    for i in range(len(a_list) - 1, 0, -1):
        for j in range(i):
            if a_list[j] > a_list[j + 1]:
                temp = a_list[j]
                a_list[j] = a_list[j + 1]
                a_list[j + 1] = temp

    for i in range(len(a_list)-1):
        if (x > a_list[i]) and (x < a_list[i + 1]):
            return a_list[i], a_list[i + 1]
        elif a_list[i] == x:
            return a_list[i], a_list[i]
    if a_list[0] > x:
        return num, a_list[0]
    elif a_list[-1] < x:
        return a_list[-1], num


if __name__ == '__main__':
    a_list = [1, 4, 6, 8, 9]
    x = 2
    print(floor_ceil(a_list, x))
    print()

    a_list = [1, 4, 6, 8, 9]
    x = 6
    print(floor_ceil(a_list, x))
    print()

    a_list = [-2, 0, 1, 3]
    x = -3
    print(floor_ceil(a_list, x))
