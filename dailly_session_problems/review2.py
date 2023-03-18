# Given an integer array, find k'th smallest element in the array where k is a positive integer less than or equal
# to the length of array.
#
# Input : [7, 4, 6, 3, 9, 1], k = 3
# Output: 4
# Explanation: The 3rd smallest array element is 4
#
# Input : [1, 5, 2, 2, 2, 5, 5, 4], k = 5
# Output: 4
# Explanation: The 5th smallest array element is 4


def kth_smallest(a_list, k):
    for i in range(len(a_list)-1, 0, -1):
        for j in range(i):
            if a_list[j] > a_list[j+1]:
                temp = a_list[j]
                a_list[j] = a_list[j+1]
                a_list[j+1] = temp
    for i in range(1, len(a_list)):
        if k == i:
            return a_list[i-1]


if __name__ == '__main__':
    print(kth_smallest([7, 4, 6, 3, 9, 1], 3))
    print(kth_smallest([1, 5, 2, 2, 2, 5, 5, 4], 5))