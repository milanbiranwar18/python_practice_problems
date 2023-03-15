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

def find_floor_ceiling(arr, x):
    # If the given number is smaller than the first element in the array,
    # then the floor doesn't exist and the ceiling is the first element
    if x < arr[0]:
        return None, arr[0]

    # If the given number is greater than the last element in the array,
    # then the ceiling doesn't exist and the floor is the last element
    if x > arr[-1]:
        return arr[-1], None

    # If the given number is equal to an element in the array,
    # then the floor and ceiling are both that element
    for i in range(len(arr)):
        if arr[i] == x:
            return arr[i], arr[i]

        # If the given number is between two elements in the array,
        # then the floor is the previous element and the ceiling is the next element
        if arr[i] < x and arr[i+1] > x:
            return arr[i], arr[i+1]


def foor_ceil(a_list, x):
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
        return num, arr[0]
    elif a_list[-1] < x:
        return arr[-1], num


if __name__ == '__main__':

    arr = [-2, 0, 1, 3]
    x = -3
    # floor, ceiling = find_floor_ceiling(arr, x)
    # print(floor, ceiling)
    # print(f"Floor of {x} is {floor}")               # Output: Floor of 9 is 8
    # print(f"Ceiling of {x} is {ceiling}")           # Output: Ceiling of 9 is 10
    #

    print(foor_ceil(arr, x))